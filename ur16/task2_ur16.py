class Mathematician:            #The class doesn't take any attributes and only has methods
    def square_nums(self, nums):          #takes a list of integers and returns the list of squares
        squares = [num ** 2 for num in nums]
        return squares

    def remove_positives(self, nums):         #takes a list of integers and returns it without positive numbers
        negatives = [num for num in nums if num < 0]
        return negatives

    def filter_leaps(self, years):         #takes a list of dates (integers) and removes those that are not 'leap years
        leap_years = [year for year in years if year % 4 == 0]
        return leap_years

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

