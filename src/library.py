import books

class Library:
    _instance = None

    @staticmethod
    def get_instance():
        if Library._instance is None:
            Library._instance = Library()
            return Library._instance

    def __init__(self):
        self.book_obj = books.Book()
        self.books_list = self.book_obj.show_books()

    def view_book(self):
        for book in self.books_list:
            print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}")

    def add_book(self,id,name,author):
        self.book_obj.add_books(id,name,author)

    def search_book(self,name):
        isBookFind = self.book_obj.search_book_by_name(name)
        if isBookFind:
            print("The book",name,"is found..")
        else:
            print("Book not available..")

    def issue_book(self,book_name):
        isFound = self.book_obj.search_book_by_name(book_name)
        if isFound:
            self.books_list = list(filter(lambda book: book[1].lower() != book_name.lower(), self.books_list))
            print("Book issued successfully")
        else:
            print("Book not available")

    def return_book(self,id,name,author):
        self.books_list.append((id,name,author))
        print("Successfully returned..")
        print(self.books_list)


