#The Guessing Game.

#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
#The result should be sent back to the user via a print statement.
import random

guess_parameter = input("Guess a number between 1 and 10: ")
random_number = random.randint(1, 10)

if not guess_parameter.isdigit():
    print('Please, enter a number between 1 and 10, not a str')
else:
    if int(guess_parameter) > 10 or int(guess_parameter) < 1:
        print('Please, enter a number between 1 and 10')
    else:
        if int(guess_parameter) != random_number:
            print('You are wrong. The right answer is ', random_number)
        else:
            print('You are right!')