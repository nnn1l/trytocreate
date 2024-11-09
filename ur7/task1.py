#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
#and the number of occurrences as values.

words = ['I', 'like', 'apples', 'also', 'I', 'like', 'tomatoes']

a_dict = {}
for word in words:
    a_dict[word] = a_dict.get(word, 0) + 1

print(a_dict)