import json

books = []


def add_book(title, author, year):
    """Add a new book to the list"""
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    print(f"Book '{title}' added successfully.")


def show_books():
    """Display all books"""
    if not books:
        print(" No books available.")
    else:
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")


def search_books(keyword):
    """Search books by title or author"""
    found = [
        book
        for book in books
        if keyword.lower() in book["title"].lower()
        or keyword.lower() in book["author"].lower()
    ]
    if not found:
        print(" No matching books found.")
    else:
        print(" Search results:")
        for i, book in enumerate(found, start=1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")


def delete_book(index):
    """Delete a book by its index"""
    if 0 < index <= len(books):
        removed = books.pop(index - 1)
        print(f" Book '{removed['title']}' deleted successfully.")
    else:
        print(" Invalid book number.")

# Test run
add_book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967)
add_book("Pride and Prejudice", "Jane Austen", 1813)
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

show_books()
