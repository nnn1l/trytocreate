value = 0
try:
    a = int(input('Enter the first number for the "a" variable: '))
    b = int(input('Enter the second number for the "b" variable : '))
    value = a**2/b
except ZeroDivisionError:
    print('"B" variable cannot be zero!')
except ValueError:
    print('Enter numbers only!')
finally:
    print(value)