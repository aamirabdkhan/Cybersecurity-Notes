# Aggregation

class Library:
	def __init__(self, name):
		self.name = name
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def list_books(self):
		return [f"{book.title} by {book.author}" for book in self.books]



class Book:
	def __init__(self, title, author):
		self.title = title
		self.author = author

library = Library("Tokyo Public Library")

book1 = Book("Harry Potter", "J. K. Rowling")
book2 = Book("The Lord of the Rings", "J. R. R. Toikien")
book3 = Book("Game of Thrones", "George R. R. Martin")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.list_books():
	print(book)