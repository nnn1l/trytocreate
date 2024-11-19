class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError('You cannot divide by zero!')
        elif isinstance(numerator, str) or isinstance(denominator, str):
            raise TypeError('The numerator and denominator mustn`t be str!')
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, application): # Задає поведінку із знаком "+"..
        if isinstance(application, Fraction):
            numerator, denominator = 0, 1
            if self.denominator == application.denominator: # Якщо знаменники однакові
                numerator = self.numerator + application.numerator
                denominator = self.denominator

            elif self.denominator % application.denominator == 0: # Знаходимо додатковий множник для другого чисельника
                numerator = int(application.numerator * self.denominator / application.denominator) + self.numerator
                denominator = self.denominator

            elif application.denominator % self.denominator == 0: # Знаходимо додатковий множник для першого чисельника
                numerator = int(self.numerator * application.denominator / self.denominator) + application.numerator
                denominator = application.denominator

            elif application.denominator % self.denominator != 0 or self.denominator % application.denominator != 0: # Знаходимо додаткові множники для обох чисельників
                numerator = self.numerator * application.denominator + application.numerator * self.denominator
                denominator = self.denominator * application.denominator

            return Fraction(numerator, denominator)

        return NotImplemented

    def __sub__(self, application):
        if isinstance(application, Fraction):
            numerator, denominator = 0, 1
            if self.denominator == application.denominator:
                numerator = self.numerator - application.numerator
                denominator = self.denominator

            elif self.denominator % application.denominator == 0:
                numerator = int(application.numerator * self.denominator / application.denominator) - self.numerator
                denominator = self.denominator

            elif application.denominator % self.denominator == 0:
                numerator = int(self.numerator * application.denominator / self.denominator) - application.numerator
                denominator = application.denominator

            elif application.denominator % self.denominator != 0 or self.denominator % application.denominator != 0:
                numerator = self.numerator * application.denominator - application.numerator * self.denominator
                denominator = self.denominator * application.denominator

            return Fraction(numerator, denominator)

        return NotImplemented

    def __mul__(self, application):
        if isinstance(application, Fraction):
            numerator = self.numerator * application.numerator
            denominator = self.denominator * application.denominator
            return Fraction(numerator, denominator)

        return NotImplemented

    def __truediv__(self, application):
        if isinstance(application, Fraction):
            numerator = self.numerator * application.denominator
            denominator = self.denominator * application.numerator
            return Fraction(numerator, denominator)

        return NotImplemented

    def __eq__(self, application):
        if self.denominator == application.denominator and self.numerator == application.numerator:
            return True
        return False

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
