from collections import namedtuple
from functools import wraps
import time


class User:
    total_users = 0
    
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        User.total_users += 1
    
    def display_info(self):
        return f"User: {self.name}"
    
    @classmethod
    def from_string(cls, data_string):
        parts = data_string.split(',')
        return cls(parts[0], parts[1], parts[2])
    
    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email


class AdminUser(User):
    def __init__(self, user_id, name, email, permissions):
        super().__init__(user_id, name, email)
        self.permissions = permissions
    
    def display_info(self):
        return f"Admin: {self.name} (Permissions: {len(self.permissions)})"


class RegularUser(User):
    def __init__(self, user_id, name, email, subscription_level):
        super().__init__(user_id, name, email)
        self.subscription_level = subscription_level
    
    def display_info(self):
        return f"Regular User: {self.name} (Level: {self.subscription_level})"


class GuestUser(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
    
    def display_info(self):
        return f"Guest: {self.name}"


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Completed: {func.__name__} in {end - start:.4f}s")
        return result
    return wrapper


def conditional_log(enabled=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"[LOG] Calling {func.__name__}")
            result = func(*args, **kwargs)
            if enabled:
                print(f"[LOG] {func.__name__} returned")
            return result
        return wrapper
    return decorator


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMING] {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper


def access_control(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'role') and self.role == required_role:
                return func(self, *args, **kwargs)
            else:
                print(f"[ACCESS DENIED] {func.__name__} requires {required_role} role")
                return None
        return wrapper
    return decorator


Config = namedtuple('Config', ['max_users', 'timeout', 'debug_mode'])


class UserManager:
    def __init__(self, config):
        self.config = config
        self.users = []
    
    def __str__(self):
        return f"UserManager with {len(self.users)} users"
    
    def __repr__(self):
        return f"UserManager(config={self.config}, users={len(self.users)})"
    
    def __len__(self):
        return len(self.users)
    
    def __eq__(self, other):
        return len(self.users) == len(other.users)
    
    def __lt__(self, other):
        return len(self.users) < len(other.users)
    
    def __call__(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    @log_execution
    def add_user(self, user):
        if len(self.users) < self.config.max_users:
            self.users.append(user)
            return True
        return False
    
    @conditional_log(enabled=True)
    def remove_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                User.total_users -= 1
                return True
        return False
    
    def user_stream(self):
        for user in self.users:
            yield user
    
    def search_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        else:
            return None


class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.role = 'admin'
    
    @timing_decorator
    def process_batch(self, batch_size):
        for i in range(0, len(self.data), batch_size):
            yield self.data[i:i + batch_size]
    
    @access_control('admin')
    def sensitive_operation(self):
        return "Sensitive data accessed"


def find_user_by_email(users, target_email):
    for user in users:
        if user.email == target_email:
            print(f"Found user: {user.name}")
            break
    else:
        print(f"No user found with email: {target_email}")


def main():
    print("=== User Management System ===\n")
    
    config = Config(max_users=100, timeout=30, debug_mode=True)
    print(f"Configuration: {config}")
    print(f"Config is immutable: {type(config).__name__}\n")
    
    manager = UserManager(config)
    
    admin = AdminUser("A001", "Alice", "alice@example.com", ["read", "write", "delete"])
    regular = RegularUser("R001", "Bob", "bob@example.com", "premium")
    guest = GuestUser("G001", "Charlie", "charlie@example.com")
    
    manager.add_user(admin)
    manager.add_user(regular)
    manager.add_user(guest)
    
    print(f"\n{manager}")
    print(f"{repr(manager)}")
    print(f"Total users in system: {User.total_users}")
    print(f"Manager length: {len(manager)}\n")
    
    user_from_string = User.from_string("U002,David,david@example.com")
    print(f"Created user from string: {user_from_string.name}")
    print(f"Email validation for 'test@example.com': {User.validate_email('test@example.com')}")
    print(f"Email validation for 'invalid': {User.validate_email('invalid')}\n")
    
    print("=== User Stream (Generator) ===")
    for user in manager.user_stream():
        print(f"  {user.display_info()}")
    
    print("\n=== Callable Manager ===")
    found_user = manager("A001")
    print(f"Called manager('A001'): {found_user.name if found_user else 'Not found'}\n")
    
    print("=== Search with Loop-Else ===")
    find_user_by_email(manager.users, "bob@example.com")
    find_user_by_email(manager.users, "nonexistent@example.com")
    
    print("\n=== Data Processing with Generators ===")
    processor = DataProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for batch in processor.process_batch(3):
        print(f"Processing batch: {batch}")
    
    print("\n=== Access Control ===")
    result = processor.sensitive_operation()
    print(f"Result: {result}")
    
    print("\n=== User Removal ===")
    manager.remove_user("G001")
    print(f"Total users after removal: {User.total_users}")
    
    print("\n=== Manager Comparison ===")
    manager2 = UserManager(config)
    manager2.add_user(RegularUser("R002", "Eve", "eve@example.com", "basic"))
    print(f"manager < manager2: {manager < manager2}")
    print(f"manager == manager2: {manager == manager2}")


if __name__ == "__main__":
    main()
