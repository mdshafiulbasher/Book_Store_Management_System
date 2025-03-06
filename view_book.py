from book_data import load_books

def view_book():
    book_list = load_books()
    if not book_list:
        print("there are no books in this system")
    else:
        for book in book_list:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: ${book['Price']:.2f}, Stock: {book['Quantity in stock']}")
