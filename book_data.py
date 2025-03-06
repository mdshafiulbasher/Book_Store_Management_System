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