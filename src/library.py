import books

class Library:
    def __init__(self):
        self.book_obj = books.Book()

    def view_book(self):
        for i in self.book_obj.show_books():
            print(i)