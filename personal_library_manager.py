import os

# Global variable to store the library
library = []

# Function to save library to a file
def save_library():
    with open('library.txt', 'w') as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read']}\n")
    print("Library saved to file.")

# Function to load library from a file
def load_library():
    if os.path.exists('library.txt'):
        with open('library.txt', 'r') as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split(',')
                read_status = read_status == 'True'
                library.append({
                    'title': title,
                    'author': author,
                    'year': int(year),
                    'genre': genre,
                    'read': read_status
                })
        print("Library loaded from file.")
    else:
        print("No library file found, starting fresh.")

# Function to add a book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'

    library.append({
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read_status
    })

    print("Book added successfully!")

# Function to remove a book from the library
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Function to search for books
def search_books():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title: ")
        results = [book for book in library if title.lower() in book['title'].lower()]
    elif choice == '2':
        author = input("Enter the author: ")
        results = [book for book in library if author.lower() in book['author'].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            read_status = 'Read' if book['read'] else 'Unread'
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Function to display all books in the library
def display_books():
    if not library:
        print("No books in the library.")
    else:
        print("Your Library:")
        for idx, book in enumerate(library, 1):
            read_status = 'Read' if book['read'] else 'Unread'
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Function to display library statistics
def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
    else:
        read_books = sum(1 for book in library if book['read'])
        percentage_read = (read_books / total_books) * 100
        print(f"Total books: {total_books}")
        print(f"Percentage read: {percentage_read:.1f}%")

# Main function to display the menu and handle user input
def main():
    load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_books()
        elif choice == '4':
            display_books()
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            save_library()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
