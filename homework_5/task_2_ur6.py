#Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

#Constraints: use only while loop and random module to generate numbers
import random

list_1 = []
list_2 = []

while len(list_1) < 10:
    list_1.append(random.randint(1, 10))
while len(list_2) < 10:
    list_2.append(random.randint(1, 10))

print('We have two lists:\n', list_1,'\n', list_2)
list_3 = list_1 + list_2
print('And if we add them together, we will get third list:\n', list_3)

mutable_numbers = 1

while mutable_numbers <= 10:
    while list_3.count(mutable_numbers)>1:
         list_3.remove(mutable_numbers)
    mutable_numbers += 1

print('But without any duplicates, third list would look like this:\n', list_3)

