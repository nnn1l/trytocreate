#String manipulation.

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

text_example = input('Write an example of text: ')
amount_chars = len(text_example)
if amount_chars >= 2:
    print(text_example[0:2] + text_example[-2:])
else:
    print('Empty string')