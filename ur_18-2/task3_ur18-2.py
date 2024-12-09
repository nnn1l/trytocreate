import functools


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def wrapper(*args):
            try:
                index = -1
                while index < len(args):
                    index += 1
                    return int(args[index])
            except ValueError:
                return None
        return wrapper

    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def wrapper(*args):
            try:
                index = -1
                while index < len(args):
                    index += 1
                    if str(args[index]).lower() == 'true':
                        return True
                    elif str(args[index]).lower() == 'false':
                        return False
            except ValueError:
                return None
        return wrapper

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def wrapper(*args):
            try:
                index = -1
                while index < len(args):
                    index += 1
                    return str(args[index])
            except ValueError:
                return None
            return wrapper

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def wrapper(*args):
            try:
                index = -1
                while index < len(args):
                    index += 1
                    return float(args[index])
            except ValueError:
                return None

        return wrapper



@TypeDecorators.to_float
def do_nothing(string: str):
    return string

@TypeDecorators.to_int
def do_nothing2(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('-2.5') == -2.5

assert do_nothing2('-25') == -25

assert do_something('True') is True

