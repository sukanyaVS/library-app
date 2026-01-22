import books

class Library:
    def __init__(self):
        self.book_obj = books.Book()
        self.books_list = self.book_obj.show_books()

    def view_book(self):
        for i in self.books_list:
            print(i)

    def add_book(self,id,name,author):
        self.book_obj.add_books(id,name,author)

    def search_book(self,name):
        isBookFind = self.book_obj.search_book_by_name(name)
        if isBookFind:
            print("The book",name,"is found..")
        else:
            print("No results found..")    



