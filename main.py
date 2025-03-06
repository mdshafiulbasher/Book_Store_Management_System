from add_book import add_book
from view_book import view_book
from search_book import search_book
from delete_book import delete_book

def display_menu():
    print("\nWelcome to the Book Store Management System!")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Thank you for using the Book Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()