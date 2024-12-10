"""
Implement a queue using a singly linked list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.root = None   
        self.size = 0      

    def push(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.front = self.root = new_node
        else:
            self.root.next_node = new_node
            self.root = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop from empty queue")
        data = self.front.data
        self.front = self.front.next_node
        if not self.front:  # If the queue becomes empty
            self.root = None
        self.size -= 1
        return data

    def get(self):
        if self.size == 0:
            raise IndexError("get from empty queue")
        return self.front.data


    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next_node
        return "Queue(front -> " + " -> ".join(items) + " -> root)"


# Example Usage
queue = Queue()

# Push items into the queue
queue.push(10)
queue.push(20)
queue.push(30)
print(queue)  #  Queue(front -> 10 -> 20 -> 30 -> root)

print(queue.get())  #  10

print(queue.pop())  #  10
print(queue)  #  Queue(front -> 20 -> 30 -> root)

print(queue.size)  #  2

print(queue.pop())  #  20
print(queue.pop())  #  30

print(queue.size)  #  0
