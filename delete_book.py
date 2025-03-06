from book_data import load_books , save_book

def delete_book():
    book_list = load_books()
    isbn = input("enter ISBN number which you wanted to delete: ")
    
    for book in book_list:
        if book["ISBN"] == isbn :
            book_list.remove(book)
            save_book(book_list)
            print("book remove successfully")
            return
    print("Book not found")
