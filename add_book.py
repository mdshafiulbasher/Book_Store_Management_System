from book_data import load_books , save_book

def add_book():
    book_list = load_books()
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    genre = input("Enter book genre: ")
    price = float(input("Enter book price: "))
    if price<=0:
        print("The price must be a positive number.")
        return
    quantity = int(input("Enter quantity in stock: "))
    if quantity <= 0:
        print("The quantity must be a non-negative integer.")
        return

    for book in book_list:
        if book["ISBN"] == isbn:
            print("Error: A book with this ISBN already exists.")
            return
    
    new_book = {
      "Title": title,
      "Author": author,
      "ISBN": isbn,
      "Genre": genre,
      "Price": price,
      "Quantity in stock": quantity
    }
    book_list.append(new_book)

    save_book(book_list)
    print("book added successfully")