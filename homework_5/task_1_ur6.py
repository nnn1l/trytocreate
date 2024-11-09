#Write a Python program to get the largest number from a list of random numbers with the length of 10

#Constraints: use only while loop and random module to generate numbers
import random

spysok = []

while len(spysok)<10:
    spysok.append(random.randint(-100, 100))

print('So, there are some numbers:\n', spysok, '\nAnd the largest number of them is...\t', max(spysok))
