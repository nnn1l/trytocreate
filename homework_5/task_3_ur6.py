#Make a list that contains all integers from 1 to 100, then find all integers from the list
#that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

#Constraint: use only while loop for iteration

list_to100 = []
variable_numbers = 1

list_only7 = []
list_only5_mult7 = []

while len(list_to100) < 100:
    list_to100.append(variable_numbers)
    if variable_numbers % 5 == 0 and variable_numbers % 7 == 0:
        list_only5_mult7.append(variable_numbers)
    elif variable_numbers % 7 == 0:
        list_only7.append(variable_numbers)
    variable_numbers += 1

print(list_only7, '\n', list_only5_mult7)
