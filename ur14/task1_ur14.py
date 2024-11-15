import inspect

def logger(func):
    def wrapper():
        print(f"{func.__name__} has arguments that called {inspect.signature(func)}")
    wrapper()

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
