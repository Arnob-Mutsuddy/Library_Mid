class Library:
    list = []

    @classmethod
    def entry_book(cls, book):
        cls.list.append(book)


class Book:
    def __init__(self, book_id, title, author, available=True):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = available
        Library.entry_book(self)

    def buy(self):
        if self._available:
            self._available = False
            return f"Book {self._title} has been borrowed."
        return f"Error: Book {self._title} is not available."

    def book_info(self):
        if self._available:
            status = "Available"
        else:
        status = "Not Available"

        return (
            f"Book ID: {self._book_id}\n"
            f"Title: {self._title}\n"
            f"Author: {self._author}\n"
            f"Status: {status}"
        )

    def return_book(self):
        if not self._available:
            self._available = True
            return f"Book {self._title} has been returned."
        return f"Error: Book {self._title} is already in the library."


def all_book():
    if not Library.list:
        print("No books in the library.")
    else:
        print("Library Books:")
        for book in Library.list:
            print("-" * 25)
            print(book.book_info())
        print("-" * 25)


def find_id(book_id):
    for book in Library.list:
        if book._book_id == book_id:
            return book
    return None


def main():

    Book(1, "Physics", "Topon")
    Book(2, "Chemistry", "Hazari Nag")
    Book(3, "Death Note", "Ohba")

    while True:
        print("\nLibrary System Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        No = input("Enter your choice (1-4): ")

        if No == "1":
            all_book()

        elif No == "2":
            book_id = input("Enter Book ID to borrow: ")
            if book_id == "1" or "2" or "3":
                book_id = int(book_id)
                book = find_id(book_id)
                if book:
                    print(book.buy())
                else:
                    print(f"Error: Book with ID {book_id} not found.")
            else:
                print("Error: Please enter a valid number for Book ID.")

        elif No == "3":
            book_id = input("Enter Book ID to return: ")
            if book_id == "1" or "2" or "3":
                book_id = int(book_id)
                book = find_id(book_id)
                if book:
                    print(book.return_book())
                else:
                    print(f"Error: Book with ID {book_id} not found.")
            else:
                print("Error: Please enter a valid number for Book ID.")

        elif No == "4":
            print("Goodbye!")
            break

        else:
            print("Error: Please enter a number between 1 and 4.")


main()
