"""
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."
"""

class Stack:
    def __init__(self):
        self._count = []

    def push(self, char):
        self._count.append(char)

    def pop(self):
        self._count.pop()

    def get(self):
        return self._count[-1]

    def __len__(self):
        return len(self._count)


def is_balanced(is_str: str):
    parentheses = Stack()
    braces = Stack()
    curly_brackets = Stack()

    for char in is_str:
        if char == '(':
            parentheses.push(char)
        elif char == ')':
            if not parentheses:
                return False
            parentheses.pop()

        if char == '[':
            braces.push(char)
        elif char == ']':
            if not braces:
                return False
            braces.pop()

        if char == '{':
            curly_brackets.push(char)
        elif char == '}':
            if not curly_brackets:
                return False
            curly_brackets.pop()

    return len(parentheses) == 0 and len(braces) == 0 and len(curly_brackets) == 0
example_1 = '()('
print(is_balanced(example_1))
example_2 = '()'
print(is_balanced(example_2))
example_3 = '{}'
print(is_balanced(example_3))
example_4 = '}{'
print(is_balanced(example_4))
example_5 = ']'
print(is_balanced(example_5))
example_6 = '[]'
print(is_balanced(example_6))
example_7 = '()[]{'
print(is_balanced(example_7))

"""
result:

False
True
True
False
False
True
False
"""