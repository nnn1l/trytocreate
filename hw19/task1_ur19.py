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
        self.list_result = []
        while self.index < self.max_index:
            if self.index < self.max_index:
                result_tuple = (self.start, self.iterable[self.index])
                self.index += 1
                self.start += 1
                self.list_result.append(result_tuple)
            else:
                raise StopIteration
        return self.list_result


x = next(WithIndex([1, 2, 3]))
print(x) #[(0, 1), (1, 2), (2, 3)]

y = next(WithIndex([1, 2, 3, 4, 5, 6], 3))
print(y) #[(3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)]