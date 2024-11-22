class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        # Basic email validation logic without using `re`
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError(f"Invalid email address: {email}")

# Usage example
try:
    user = User("example@domain.com")
    print(f"Valid email: {user.email}")
except ValueError as e:
    print(e)

try:
    user = User("invalid-email")
    print(f"Valid email: {user.email}")
except ValueError as e:
    print(e)