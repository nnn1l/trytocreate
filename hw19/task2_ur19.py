# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 'start', 'end', and optional step.

def in_range(start, end, step=1):
    if not isinstance(start or end or step, int): # checks if all arguments are integers
        raise TypeError('All values must be integers')

    if step == 0:
        raise ValueError('Step must not equal 0')

    elif start < end:
        if step > 0:
            while start < end:
                yield start
                start += step
        else:
            return None

    elif start > end:
        if step < 0:
            while start > end:
                yield start
                start += step
        else:
            return None

    else:
        return None

for value in in_range(0, 16, 3):
    print(value) # -> 0, 3, 6, 9, 12, 15

print('----'*10)

for value in in_range(15, 0, -3):
    print(value) # -> 15, 12, 9, 6, 3

for value in in_range(5, 0):
    print(value)  # -> None, because 5>0 and step > 0 (step default 1)
