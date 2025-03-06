import json

def load_books(filename = "books.json"):
    try:
        with open (filename , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return "file not found"
    
def save_book(book_list , filename = "books.json"):
    with open(filename, 'w') as file:
        return json.dump(book_list, file , indent=4)

# books = load_books()
# for book in books:
#     print(type(book["ISBN"]))
# books = "books.json"
# load_books(books)
# # print(load_books(books))

# new_book = {
#       "Title": "1984_1",
#       "Author": "George Orwell",
#       "ISBN": "11",
#       "Genre": "Dystopian",
#       "Price": 8.99,
#       "Quantity in stock": 75
#     }
# book = load_books()
# print(book)
# book.append(new_book)
# save_book(book)
# print(load_books(books))