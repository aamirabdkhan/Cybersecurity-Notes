# Magic Methods

class Book:

	def __init__(self, title, author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	def __str__(self):
		return f"{self.title} by {self.author}"

	def __eq__(self, other):
		return self.title == other.title and self.author == other.author

	def __lt__(self, other):
		return self.pages < other.pages

	def __gt__(self, other):
		return self.pages > other.pages

	def __add__(self, other):
		return f"{self.pages + other.pages}pages"

	def __contains__(self, keyword):
		return keyword in self.title or keyword in self.author

	def __getitem__(self, key):
		if key == "title":
			return self.title
		elif key == "author":
			return self.author
		elif key == "pages":
			return self.pages
		else:
			return f"key '{key}' was not found"

book1 = Book("The Lord of the Rings", "J. R. R. Toikien", 320)
book2 = Book("Harry Potter", "J. K. Rowling", 244)
book3 = Book("Game of Thrones", "George R. R. Martin", 466)
book4 = Book("Harry Potter", "J. K. Rowling", 456)

print(book1)
print(book2 == book4)
print(book2 < book3)
print(book2 > book3)
print(book2 + book4)
print("Lord" in book1)
print("Lord" in book3)
print("Rowling" in book1)
print(book1["title"])
print(book2["author"])
print(book3["pages"])
print(book4["video"])