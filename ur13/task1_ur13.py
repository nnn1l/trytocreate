import inspect

def amount_of_arg(func):
    print(len(inspect.signature(func).parameters))

def make_operation(operand, *args):
    value1 = 0
    if operand == '+':
        return sum(args)
    elif operand == '-':
        for minus in args:
            value1 -= minus
    elif operand == '*':
        value1 = 1
        for multiplied in args:
            value1 *= multiplied
    return value1

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))

amount_of_arg(make_operation)