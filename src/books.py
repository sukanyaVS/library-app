books_list = [
    ("B101", "Python Basics", "Guido van Rossum"),
    ("B102", "Data Structures", "Mark Allen Weiss"),
    ("B103", "Clean Code", "Robert C. Martin"),
    ("B104", "Operating Systems", "Abraham Silberschatz"),
    ("B105", "Database Systems", "C. J. Date")
]


class Book():
    def __init__(self):
        pass

    def show_books(self):
        return books_list
    
    def add_books(self,id,name,author):
        self.id = id
        self.name = name
        self.author = author
        books_list.append((self.id,self.name,self.author))
        print("Successfully added..")
        print(books_list)

    def search_book_by_name(self,name):
        isFound = False
        name = name.lower()
        for book in books_list:
            if name == book[1].lower():
                isFound = True
                break
            else:
                isFound = False
        return isFound        