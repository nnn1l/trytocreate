#Words combination

#Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.
import random

text = input('Write everything you want: ')
amount_ofChars = len(text)

word_list = []

for i in range(5):
    for a in range(amount_ofChars):
        generated_letter = random.choice(text)
        word_list.append(generated_letter)
    print(word_list)
    word_list = []