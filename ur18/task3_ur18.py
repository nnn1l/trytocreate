import functools



class TypeDecorators:

    @classmethod
    def to_int(cls, func):
        @functools.wraps(func)
        def wrapper(*args):
            index = -1
            while index < len(args):
                index += 1
                if args[index].replace('-', '0').isnumeric() is True:
                    return int(args[index])
                else:
                    return args[index]
        return wrapper

    @classmethod
    def to_bool(cls, func):
        @functools.wraps(func)
        def wrapper(*args):
            index = -1
            while index < len(args):
                index += 1
                if args[index].lower() == 'true':
                    return True
                elif args[index].lower() == 'false':
                    return False
                else:
                    return args[index]
        return wrapper

    @classmethod
    def to_str(cls, func):
        @functools.wraps(func)
        def wrapper(*args):
            index = -1
            while index < len(args):
                index += 1
                return str(args[index])
        return wrapper

    @classmethod
    def to_float(cls, func):
        @functools.wraps(func)
        def wrapper(*args):
            index = -1
            while index < len(args):
                index += 1
                if args[index].replace('.', "0").replace('-', '0').isnumeric() is True:
                    return float(args[index])
                else:
                    return args[index]
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

