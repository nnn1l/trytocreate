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
    else:
        raise ValueError(f'Operand {operand} not supported')
    return value1
