# Library Management System using a dictionary

library = {}  # Dictionary to store library books

# Function to add a book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    quantity = int(input("Enter the quantity available: "))

    if isbn in user_library:
        print("Book with the same ISBN already exists in your library.")
        return

    # Create a book dictionary
    book = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Quantity": quantity
    }

    # Add the book to user_library
    user_library[isbn] = book
    print("Book added successfully!")


# Function to update book information in the library
def update_book():
    isbn = input("Enter the ISBN of the book to update: ")

    # Combine the sample book data with the user's library
    combined_library = book_data + list(user_library.values())

    for book in combined_library:
        if book["ISBN"] == isbn:
            print("Current book information:")
            print(book)
            title = input("Enter the new title (leave empty to keep the same): ")
            author = input("Enter the new author (leave empty to keep the same): ")
            quantity = input("Enter the new quantity (leave empty to keep the same): ")

            if title:
                book["Title"] = title
            if author:
                book["Author"] = author
            if quantity:
                book["Quantity"] = int(quantity)

            print("Book information updated!")
            return

    print("Book not found in the library.")

# Function to search for a book in the library
def search_book():
    search_term = input("Enter the book title, author, or ISBN to search: ")

    # Combine the sample book data with the user's library
    combined_library = book_data + list(user_library.values())

    found_books = []
    for book in combined_library:
        if (search_term in book["Title"]) or (search_term in book["Author"]) or (search_term in book["ISBN"]):
            found_books.append(book)

    if found_books:
        print("Books found:")
        for book in found_books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Quantity: {book['Quantity']}")
    else:
        print("No books found in the library matching your search.")

book_data = [
    {
        "Title": "Karachi to Australia",
        "Author": "Chota chungus",
        "ISBN": "10",
        "Price": 1200,
        "Quantity": 50
    },
    {
        "Title": "1989",
        "Author": "George Washington",
        "ISBN": "20",
        "Price": 999,
        "Quantity": 30
    },
    {
        "Title": "The Great Civil war",
        "Author": "Tomianz",
        "ISBN": "30",
        "Price": 1149,
        "Quantity": 25
    },
]
# User's library
user_library = {}

# Function to list all books in the library
def list_books():
    # Merge the user's library with the initial dataset
    combined_library = book_data + list(user_library.values())

    if combined_library:
        for book in combined_library:
            print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Quantity: {book['Quantity']}")
    else:
        print("No books in the library.")

# Function to borrow a book from the library
def borrow_book():
    isbn = input("Enter the ISBN of the book to borrow: ")

    # Combine the sample book data with the user's library
    combined_library = book_data + list(user_library.values())

    for book in combined_library:
        if book["ISBN"] == isbn:
            if book["Quantity"] > 0:
                book["Quantity"] -= 1
                print("Book borrowed successfully!")
            else:
                print("This book is not available for borrowing.")
            return

    print("Book not found in the library.")

# Function to return a book to the library
def return_book():
    isbn = input("Enter the ISBN of the book to return: ")

    # First, check if the book is in user's library
    if isbn in user_library:
        user_library[isbn]["Quantity"] += 1
        print("Book returned successfully from your library.")
    else:
        # If not found in user's library, check the sample book data
        for book in book_data:
            if book["ISBN"] == isbn:
                book["Quantity"] += 1
                print("Book returned successfully from the library.")
                return
        print("Book not found in the library.")

# Function to delete a book from the library
def delete_book():
    isbn = input("Enter the ISBN of the book to delete: ")

    # First, check if the book is in user's library
    if isbn in user_library:
        del user_library[isbn]
        print("Book deleted from your library.")
    else:
        # If not found in user's library, check the sample book data
        for book in book_data:
            if book["ISBN"] == isbn:
                print("You cannot delete books from the sample data.")
                return
        print("Book not found in your library.")

def display_book_prices():
    for book in book_data:
        print(f"Title: {book['Title']}")
        print(f"ISBN: {book['ISBN']}")
        print(f"Price: ${book['Price']:.2f}")
        print("")
def restock_books():
    for book in book_data:
        if book['Quantity'] < 10:
            print(f"Restocking {book['Title']} (ISBN: {book['ISBN']})")
            book['Quantity'] += 50
            print("Restocked successfully")
        else:
            print("Stock does not need to refilled")
# Main program loop
while True:
    print("\nLibrary Management System Menu:")
    print("1. User menu")
    print("2. Admin Menu")
    print("3. Exit")

    main_choice = input("Enter your choice (1-3): ")

    if main_choice == "1":
        # Library Functions
        while True:
            print("\nUser menu:")
            print("1. List All Books")
            print("2. Search for a Book")
            print("3. Borrow a Book")
            print("4. Return a Book")
            print("5. Back to Main Menu")

            library_choice = input("Enter your choice (1-5): ")
            if library_choice == "1":
                list_books()
            elif library_choice == "2":
                search_book()
            elif library_choice == "4":
                list_books()
            elif library_choice == "3":
                borrow_book()
            elif library_choice == "4":
                return_book()
            elif library_choice == "5":
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    elif main_choice == "2":
        # Admin Menu (Option 2)
     while True:
        print("\nAdmin Menu ")
        print("1. Add a Book")
        print("2. Update Book Information")
        print("3. Delete a Book")
        print("4. Watch prices of books available")
        print("5. Restock the books")
        print("6. Back to Main Menu")
        admin_choice = input("Enter your choice :")
        # admin controls and functions
        if admin_choice == "1":
            add_book()
        elif admin_choice == "2":
            update_book()
        elif admin_choice == "3":
            delete_book()
        elif admin_choice == "4":
            display_book_prices()
        elif admin_choice == "5":
            restock_books()
        elif admin_choice == "6":
            break
        else:
                print("Invalid choice. Please enter a valid option.")
    # Main menu continues here
    elif main_choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")


