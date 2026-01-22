from library import Library

def main():
    print("Welcome!")
    print("......Library Menu......")
    print("1. View All Books")
    print("2. Add Book")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Register User")
    print("7. Exit")

    choice = input("Enter your choice : ")
    lib_obj = Library.get_instance()

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
        case "4":
            book_name = input("Enter the book's name to borrow : ")
            lib_obj.issue_book(book_name) 
        case "5":
            id = input("Enter book id: ")
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            lib_obj.return_book(id,name,author) 
        case "6":
            print("Learn more...Thank you")       
        case _:
            print("Invalid choice")

main()