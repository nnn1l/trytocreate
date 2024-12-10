"""
Implement a stack using a singly linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.root
        self.root = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty stack")
        data = self.root.data
        self.root = self.root.next_node
        self.size -= 1
        return data

    def __str__(self):
        items = []
        current = self.root
        while current:
            items.append(str(current.data))
            current = current.next_node
        return "Stack(root -> " + " -> ".join(items) + ")"



stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)  #  Stack(root -> 30 -> 20 -> 10)

print(stack.pop())  #  30
print(stack.pop())  #  20
print(stack)  #  Stack(root -> 10)

print(stack.size)  #  1

print(stack.pop())  #  10
print(stack.size)  #  0
