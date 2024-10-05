#The math quiz program

#Write a program that asks the answer for a mathematical expression,
#checks whether the user is right or wrong, and then responds with a message accordingly.
a = 25
b = 15
c = -12
d = 6

math_expression1 = int(input('25 + 15 = '))
math_expression2 = int(input('-12 - 6 = '))

if math_expression1 != a+b:
    print('The first answer is incorrect')
else:
    print('The first answer is correct')
if math_expression2 != c-d:
    print('The second answer is incorrect')
else:
    print('The second answer is correct')

