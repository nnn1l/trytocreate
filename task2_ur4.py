#The valid phone number program

#Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

number_phone = input('Enter a phone number: ')

if len(number_phone) != 10:
    print('Please enter 10 numbers.')
elif not number_phone.isdigit():
    print('The number phone cannot be converted to an integer.')
else:
    print('Thank you!')