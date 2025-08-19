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
