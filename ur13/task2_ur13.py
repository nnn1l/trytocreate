def summary(a, b):
    print('Summary:', float(a)+float(b))
    def summary_in_exp(n):
        print('Summary in exp:', (float(a)+float(b))**int(n))
    summary_in_exp(input("Enter a number of exponentiation: "))

try:
    summary(input("Enter a number for a variable A: "), input("Enter a number for a variable B: "))
except ValueError:
    print("Please enter a number")