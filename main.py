import json
from collections import Counter

books = []
FILE_NAME = "books.json"


def load_books():
    global books
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            books = json.load(f)
        print(f" Loaded {len(books)} books from '{FILE_NAME}'.")
    except FileNotFoundError:
        print(f"File '{FILE_NAME}' not found. Starting with empty library.")
        books = []

def save_books():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print(f" Saved {len(books)} books to '{FILE_NAME}'.")


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    if title and author and year:
        books.append({"title": title, "author": author, "year": year})
        print(f" Book '{title}' added successfully.")
    else:
        print("All fields are required!")

def show_books():
    if not books:
        print(" No books available.")
    else:
        print("\nList of Books:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")
        print()


def search_books():
    keyword = input("Enter title or author to search: ").strip()
    found = [
        b
        for b in books
        if keyword.lower() in b["title"].lower()
        or keyword.lower() in b["author"].lower()
    ]
    if not found:
        print(" No matching books found.")
    else:
        print("\nSearch Results:")
        for i, book in enumerate(found, start=1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")
        print()


def delete_book():
    show_books()
    try:
        index = int(input("Enter the book number to delete: "))
        if 0 < index <= len(books):
            removed = books.pop(index - 1)
            print(f" Book '{removed['title']}' deleted successfully.")
        else:
            print(" Invalid book number.")
    except ValueError:
        print(" Please enter a valid number.")


def update_book():
    show_books()
    try:
        index = int(input("Enter the book number to update: "))
        if 0 < index <= len(books):
            book = books[index - 1]
            print("Leave blank to keep current value.")
            title = input(f"New title [{book['title']}]: ").strip() or book["title"]
            author = input(f"New author [{book['author']}]: ").strip() or book["author"]
            year = input(f"New year [{book['year']}]: ").strip() or book["year"]
            books[index - 1] = {"title": title, "author": author, "year": year}
            print(f" Book '{title}' updated successfully.")
        else:
            print(" Invalid book number.")
    except ValueError:
        print(" Please enter a valid number.")


def sort_books():
    if not books:
        print(" No books to sort.")
        return
    print("\nSort by:")
    print("1. Title (A-Z)")
    print("2. Author (A-Z)")
    print("3. Year (ascending)")
    print("4. Year (descending)")
    choice = input("Choose an option (1-4): ").strip()
    if choice == "1":
        books.sort(key=lambda b: b["title"].lower())
    elif choice == "2":
        books.sort(key=lambda b: b["author"].lower())
    elif choice == "3":
        books.sort(key=lambda b: int(b["year"]))
    elif choice == "4":
        books.sort(key=lambda b: int(b["year"]), reverse=True)
    else:
        print(" Invalid choice.")
        return
    print(" Books sorted successfully.")
    show_books()


def statistics():
    print("\n Library Statistics:")
    total = len(books)
    print(f"Total books: {total}")
    if total > 0:
        authors = [b["author"] for b in books]
        counter = Counter(authors)
        print("Books per author:")
        for author, count in counter.items():
            print(f"- {author}: {count}")


def main_menu():
    load_books()
    while True:
        print("\n=== Advanced Library System ===")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Search books")
        print("4. Delete a book")
        print("5. Update a book")
        print("6. Sort books")
        print("7. Statistics")
        print("8. Save and exit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            sort_books()
        elif choice == "7":
            statistics()
        elif choice == "8":
            save_books()
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main_menu()
