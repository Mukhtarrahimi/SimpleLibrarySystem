import json

# List of books
books = []

FILE_NAME = "books.json"


def load_books():
    """Load books from a JSON file"""
    global books
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            books = json.load(f)
        print(f" Loaded {len(books)} books from '{FILE_NAME}'.")
    except FileNotFoundError:
        print(f"File '{FILE_NAME}' not found. Starting with empty library.")
        books = []


def save_books():
    """Save books to a JSON file"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print(f" Saved {len(books)} books to '{FILE_NAME}'.")


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


# -----------------------------
def main_menu():
    load_books()
    while True:
        print("\n=== Simple Library System ===")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Search books")
        print("4. Delete a book")
        print("5. Save and exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            save_books()
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main_menu()
