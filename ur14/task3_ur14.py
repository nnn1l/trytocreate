def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(func):
        def inner(*args, **kwargs):
            arg = args[0]
            if not isinstance(arg, type_):     # Check if argument is of the correct type
                print("The slogan is not a string.")
                return False
            elif len(arg) > max_length:        # Check if argument exceeds the maximum length
                print("The slogan is too long. Maximum length is {}.".format(max_length))
                return False
            elif not all(words in arg for words in contains):      # Check if argument contains all required substrings
                print("The slogan does not contain {}.".format(contains))
                return False
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper



@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
