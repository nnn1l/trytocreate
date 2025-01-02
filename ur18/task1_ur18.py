class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email): # checks if email is written right
        if '@' in email: #checks if email has '@'
            mail, domen = email.split('@')
            first_last = [mail[0], mail[-1], domen[0], domen[-1]]
            if '.' not in first_last and '-' not in first_last: #checks if mail and domain has not '-' or '.' on the start or end
                print(f'Valid email: {email}')
            else:
                print(f'Invalid email: {email}')
        else: # If check is failed, printed invalid email
            print(f'Invalid email: {email}')


user1 = User("example@domain.com")
user2 = User("invalid-@email.com")
user3 = User("invalidemail.com")

