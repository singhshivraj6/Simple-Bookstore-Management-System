{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Define a list to store books\
books = []\
\
# Function to add a book to the bookstore\
def add_book(title, author, isbn, quantity):\
    book = \{"title": title, "author": author, "isbn": isbn, "quantity": quantity\}\
    books.append(book)\
    print("Book added successfully!")\
\
# Function to remove a book by ISBN\
def remove_book(isbn):\
    for book in books:\
        if book["isbn"] == isbn:\
            books.remove(book)\
            print("Book removed successfully!")\
            return\
    print("Book not found.")\
\
# Function to list all books\
def list_books():\
    if not books:\
        print("No books in the bookstore.")\
    else:\
        print("List of Books:")\
        for book in books:\
            print(f"Title: \{book['title']\}, Author: \{book['author']\}, ISBN: \{book['isbn']\}, Quantity: \{book['quantity']\}")\
\
# Function to search for a book by ISBN\
def search_book(isbn):\
    for book in books:\
        if book["isbn"] == isbn:\
            print("Book found:")\
            print(f"Title: \{book['title']\}, Author: \{book['author']\}, ISBN: \{book['isbn']\}, Quantity: \{book['quantity']\}")\
            return\
    print("Book not found.")\
\
# Main menu\
while True:\
    print("\\nBookstore Management Menu:")\
    print("1. Add a book")\
    print("2. Remove a book")\
    print("3. List all books")\
    print("4. Search for a book")\
    print("5. Quit")\
\
    choice = input("Enter your choice: ")\
\
    if choice == "1":\
        title = input("Enter book title: ")\
        author = input("Enter author name: ")\
        isbn = input("Enter ISBN: ")\
        quantity = input("Enter quantity: ")\
        add_book(title, author, isbn, quantity)\
    elif choice == "2":\
        isbn = input("Enter ISBN of the book to remove: ")\
        remove_book(isbn)\
    elif choice == "3":\
        list_books()\
    elif choice == "4":\
        isbn = input("Enter ISBN of the book to search: ")\
        search_book(isbn)\
    elif choice == "5":\
        print("Goodbye!")\
        break\
    else:\
        print("Invalid choice. Please try again.")\
}