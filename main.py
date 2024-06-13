# used additional stuffs learned during the oop sessions to improved, I also looked at examples for syntaxes
class Book:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id
        self.is_borrowed = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            return book.title + " has been borrowed by " + self.name
        return book.title + " is not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return book.title + " has been returned by " + self.name
        return "book was not borrowed by this member"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, book_id):
        if book_id not in self.books:
            self.books[book_id] = Book(title, book_id)
            return "book '" + title + "' added to the library"
        return "book id exists"

    def add_member(self, name, member_id):
        if member_id not in self.members:
            self.members[member_id] = Member(name, member_id)
            return "member '" + name + "' added to the library"
        return "member id exists"

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            return self.members[member_id].borrow_book(self.books[book_id])
        return "member or book not found"

    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            return self.members[member_id].return_book(self.books[book_id])
        return "member or book not found"

# test
library = Library()
print(library.add_book("recipe book", "b1"))
print(library.add_book("bio", "b2"))
print(library.add_member("john", "m1"))
print(library.add_member("dave", "m2"))

print(library.borrow_book("m2", "b1"))
print(library.borrow_book("m1", "b2"))
print(library.return_book("m1", "b1"))
print(library.add_member("james", "m1"))