import library

def main():
    print("Welcome!")
    print("......Library Menu......")
    print("1. View All Books")
    print("2. Add Book")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Register User")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice : ")
    lib_obj = library.Library()

    match choice:
        case "1":
            lib_obj.view_book()
        case "2":
            id = input("Enter book's id : ")
            name = input("Enter name of the book : ")
            author = input("Enter author of the book : ")
            lib_obj.add_book(id,name,author) 
        case "3":
            book_name = input("Enter name of the book : ")
            lib_obj.search_book(book_name)     
        case _:
            print("Invalid choice")

main()