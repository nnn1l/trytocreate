# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements using square brackets syntax.

class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self): # Returns an iterator object. This method is called when iterating in a for-in loop.
        return iter(self.data)

    def __getitem__(self, index): # Enables element retrieval using square brackets
        return self.data[index]


custom_iterable = CustomIterable([10, 20, 30, 40])

for item in custom_iterable:
    print(item)

print('----'*10)

print(custom_iterable[0])  # 10
print(custom_iterable[2])  # 30