import json

books = []


def add_book(title, author, year):
    """Add a new book to the list"""
    book = {"title": title, "author": author, "year": year}
