import library


books = [
    {
        "title": "soo_va_shoon",
        "author": "simin_daneshvar"
    },
    {
        "title": "palace",
        "author": "kafka"
    }
]

my_library = library.Library(books)


if __name__ == "__main__":
    commands = ['add', 'remove', 'search', 'show']
    print("You can 'add' 'remove' 'search' a book or 'show' the book list.")
    wrong_command = True
    while(wrong_command):
        try:
            command = input("Please tell me what do you want to do: ")
            if command in commands:
                wrong_command = False
            else:
                raise("Wrong command enterd!")
        except(ValueError):
            print(ValueError)
            command = input("Please tell me what do you want again: ")


