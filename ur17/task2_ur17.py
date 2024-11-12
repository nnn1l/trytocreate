class Library:
    books = []
    authors = []

    def __init__(self, name):
        self.name = name


    def new_book(self, name: str, year: int, author):  # returns an instance of Book class and adds the book to the books list for the current library.
        book = Book(name, year, author)

        if author not in Library.authors:
            Library.authors.append(author)

        Library.books.append(book)
        Author.books.append(book)
        Book.amount += 1

        return book


    def group_by_author(self, author):  # returns a list of all books grouped by the specified author
        group = [book for book in self.books if book.author == author ]

        return group


    def group_by_year(self, year: int):  # returns a list of all the books grouped by the specified year
        group = [book for book in self.books if book.year == year]

        return group


    def __str__(self):
        return f'Welcome to {self.name}! There are {len(self.books)} books, which are written by {len(self.authors)} authors.'


    def __repr__(self):
        return f'Welcome to {self.name}! There are {len(self.books)} books, which are written by {len(self.authors)} authors.'



class Book:
    amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author


    def __str__(self):
        return f'{self.name} {self.year} {self.author}'


    def __repr__(self):
        return f'{self.name} {self.year} {self.author}'



class Author:
    books = []

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday


    def __str__(self):
        return f'{self.name} {self.birthday} {self.country}'


    def __repr__(self):
        return f'{self.name} {self.birthday} {self.country}'


# Create authors
author1 = Author("J.K. Rowling", "UK", "1965-07-31")
author2 = Author("George Orwell", "UK", "1903-06-25")

# Create a library
library = Library("City Library")

# Add books
library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
library.new_book("1984", 1949, author2)
library.new_book("Animal Farm", 1945, author2)

# Group by author
print(library.group_by_author(author1))  # Books by J.K. Rowling
print(library.group_by_author(author2))  # Books by George Orwell

# Group by year
print(library.group_by_year(1997))  # Books published in 1997

# Library and book count
print(library)  # Library details
print(Book.amount)  # Total book count




