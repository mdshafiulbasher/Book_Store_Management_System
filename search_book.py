from book_data import load_books

def search_book():
    book_list = load_books()
    while True:
        print("Which category you want to search?")
        print("1. Title")
        print("2. ISBN")
        print("3. Author")
        print("4. Genre")
        choice = input("Enter a Option: ")
        if choice == '1':
            search = input("Search with Title: ")
            for book in book_list:
                if search == book["Title"]:
                    print(book)
                    return
            print("No Title Match")        
            return
        if choice == '2':
            search = input("Search with ISBN: ")
            for book in book_list:
                if search == book["ISBN"]:
                    print(book)
                    return
            print("No ISBN Match")
            return
        if choice == '3':
            search = input("Search with Author: ")
            for book in book_list:
                if search == book["Author"]:
                    print(book)
                    return
            print("No Author Match")
            return
        if choice == '4':
            search = input("Search with Genre: ")
            for book in book_list:
                if search == book["Genre"]:
                    print(book)
                    return
            print("No Genre Match")
            return
        print("please enter a option......")


    