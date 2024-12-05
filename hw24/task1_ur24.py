"""
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.
"""


class Stack:
    def __init__(self):
        self._characters = []

    def push(self, word):  # Adds each character to a list separately
        for char in word:
            self._characters.append(char)

    def pop(self):  # Deleting last character from a list
        self._characters.pop()

    def get(self): # Returns last character from a list
        return self._characters[-1]

    def __str__(self):
        return str(self._characters)

normal_str = 'Hello, my dear friend!'

def reverse(word):
    stack = Stack()
    stack.push(word)
    reversed_word = ''
    for i in word:
        reversed_word += stack.get()
        stack.pop()
    return reversed_word

print(f'{normal_str}\n{reverse(normal_str)}')
