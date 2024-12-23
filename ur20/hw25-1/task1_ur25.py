"""
Extend UnsortedList

Implement append, index, pop, insert methods for UnsortedList.
Also implement a slice method, which will take two parameters 'start' and 'stop', and return a copy of the list starting at the position and going up to but not including the stop position.
"""

class DoubleNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class UnsortedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def index(self, data): #Returns data`s index
        current = self.first
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next_node
            index += 1
        raise IndexError('data not found')

    def append(self, data):
        new_node = DoubleNode(data)
        if not self.first:
            self.first = self.last = new_node
        else:
            self.last.next_node = new_node
            new_node.prev_node = self.last
            self.last = new_node
        self.length += 1

    def append_index_0(self, data):
        new_node = DoubleNode(data)
        if not self.first:
            self.first = self.last = new_node
        else:
            new_node.next_node = self.first
            self.first.prev_node = new_node
            self.first = new_node
        self.length += 1

    def remove(self, data):
        current = self.first
        while current:
            if current.data == data:
                if current == self.first and current == self.last:
                    self.first = self.last = None

                elif current == self.first:
                    self.first = current.next_node
                    self.first.prev = None

                elif current == self.last:
                    self.last = current.prev_node
                    self.last.next = None

                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                self.length -= 1
                return
            current = current.next_node


    def pop(self): # Deletes and returns last data
        current = self.last
        returning = current.data
        self.last = current.prev_node
        self.last.next_node = None
        self.length -= 1
        return returning

    def insert(self, index, data):
        if index > self.length:
            raise IndexError('index out of range')

        new_node = DoubleNode(data)
        if index == 0:
            self.append_index_0(data)

        elif index == self.length or index == -1:
            self.append(data)

        else:
            current = self.first
            while current:
                if self.index(current.data) == index:
                    prev = current.prev_node
                    prev.next_node = new_node
                    new_node.prev_node = prev
                    new_node.next_node = current
                    current.prev_node = new_node
                current = current.next_node
        self.length += 1


    def slice(self, start, stop):
        if start < 0: start += self.length # do integers positive, if they`re negative
        if stop < 0: stop += self.length ## do integers positive, if they`re negative

        if start >= stop:
            raise IndexError('stop index must be after start index')
        if stop >= self.length:
            raise IndexError('index out of range')

        sliced = []
        current = self.first
        while self.index(current.data) < stop:
            if self.index(current.data) >= start:
                sliced.append(current.data)
            current = current.next_node
        return list(sliced)




    def __str__(self):
        n = self.first
        s = "["
        if n:
            while n.next_node:
                s += str(n.data) + ", "
                n = n.next_node

            s += str(n.data)
        s += "]"
        return s


double_linked_list = UnsortedList()

double_linked_list.append(1)
double_linked_list.append(2)
double_linked_list.append_index_0(0)
double_linked_list.append_index_0(-1)

#print(double_linked_list.index(1))
#print(double_linked_list.index('r'))
double_linked_list.insert(1, 4) # [-1, 0, 1, 2] -> [-1, 4, 0, 1, 2]
print(double_linked_list)
double_linked_list.slice(1, -1) #[4, 0, 1]ю