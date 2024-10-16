# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (+, -, *)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

def make_operation(operand, *args):
    value1 = 0
    if operand == '+':
        for plus in args:
            value1 += plus
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

