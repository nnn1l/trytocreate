#Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

squares = [(i, j**2) for i in range(1,11) for j in range(1, 11) if j == i]
print(squares)