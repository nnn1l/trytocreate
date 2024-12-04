# Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters: 'iterable' and 'start', default is 0


class WithIndex:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start
        self.index = 0
        self.max_index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max_index:
            result_tuple = (self.start, self.iterable[self.index])
            self.index += 1
            self.start += 1
        else:
            raise StopIteration
        return result_tuple

x = WithIndex([1, 2, 3])
for i in x:
    print(i) #[(0, 1), (1, 2), (2, 3)]

print('----' * 5)

y = WithIndex([1, 2, 3, 4, 5, 6], 3)
for i in y:
    print(i) #[(3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)]