from dbm.ndbm import library


class Book:
    def __init__(self, title, author, pageCount):
        self.title = title
        self.author = author
        self.pageCount = pageCount


class Library:
    library = set()  # blazingly fast, does not allow duplicates

    def get_input():
        title = input("Enter title")
        author = input("Enter author")
        pageCount = input("Enter page count")
        return Book(title, author, pageCount)

    def addBook(self):
        newBook = self.get_input()
        print(newBook.title)


l = Library()
quit = False

while (quit == False):
    print("Enter 0 to quit")
    print("Enter 1 to add a book")
    print("Enter 2 to search for a book title")
    print("Enter 3 to update a book")
    print("Enter 4 to delete a book")
    choice = input()
    if choice == '0':
        quit = True
    elif choice == '1':
        l.addBook()
