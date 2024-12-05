"""
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_queue that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message
"""

class Stack:
    def __init__(self):
        self._order = []

    def push(self, e):
        self._order.append(e)

    def pop(self):
        self._order.pop()

    def get(self):
        return self._order[-1]

    def get_from_stack(self, e):
        element = len(self._order) - 1
        while element >= 0:
            if not self._order[element] == e:
                element -= 1
            elif self._order[element] == e:
                print(f'Your element {e} was found in the stack by the index {element}')
                break
        else:
            raise ValueError(f'Your element {e} was not found in the stack')




class Queue:
    def __init__(self):
        self._order = []

    def push(self, e):
        self._order.append(e)

    def pop(self):
        self._order.pop(0)

    def get(self):
        return self._order[0]

    def get_from_queue(self, e):
        element = 0
        while element < len(self._order):
            if not self._order[element] == e:
                element += 1
            elif self._order[element] == e:
                print(f'Your element {e} was found in the queue by the index {element}')
                break
        else:
            raise ValueError(f'Your element {e} was not found in the queue')


stack = Stack()
queue = Queue()

str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in str_list:
    stack.push(i)
    queue.push(i)

stack.get_from_stack('f') # -> Your element f was found in the stack by the index 5
queue.get_from_queue('e') # -> Your element e was found in the queue by the index 4

stack.get_from_stack(1) # -> ValueError: Your element 1 was not found in the stack
queue.get_from_queue(2) # -> ValueError: Your element 2 was not found in the queue