
class Library:
    books = []

    def __init__(self, books):
        self.books = books

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }

        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                del book
                break

    def search_book(self, title):
        found = False
        foubd_index = 0
        
        for book, index in self.books:
            if book.title == "title":
                found = True
                found_index = index
                break
        
        if found:
            print(f"The {title} book is found. It's book no. {index} in the book list.")
        else:
            print(f"There is no book with the {title} title!")
        
    def show_books(self):
        book_count = len(self.books)
        print(f"There are {book_count} in the list.")
        if book_count > 0:
            print(f"These are the books in our list: {self.books}")