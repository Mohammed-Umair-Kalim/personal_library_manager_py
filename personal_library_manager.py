import json
import streamlit as st

# Initialize the library as an empty list
library = []

# File to save and load the library
LIBRARY_FILE = "library.json"

def load_library():
    """Load the library from a file if it exists."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

def add_book():
    """Add a book to the library."""
    st.header("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read Status (Checked if read)")
    
    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read_status": read_status
        }
        library.append(book)
        save_library()
        st.success(f"Book '{title}' added successfully!")

def remove_book():
    """Remove a book from the library by title."""
    st.header("Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    
    if st.button("Remove Book"):
        global library
        library = [book for book in library if book["title"].lower() != title.lower()]
        save_library()
        st.success(f"Book '{title}' removed successfully!")

def search_books():
    """Search for books by title or author."""
    st.header("Search for a Book")
    search_term = st.text_input("Enter title or author to search")
    
    if st.button("Search"):
        results = [
            book for book in library
            if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()
        ]
        if results:
            st.write("Search Results:")
            for book in results:
                st.write(format_book(book))
        else:
            st.write("No matching books found.")

def display_all_books():
    """Display all books in the library."""
    st.header("All Books")
    if library:
        for book in library:
            st.write(format_book(book))
    else:
        st.write("The library is empty.")

def display_statistics():
    """Display library statistics."""
    st.header("Library Statistics")
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    st.write(f"Total Books: {total_books}")
    st.write(f"Percentage Read: {percentage_read:.2f}%")

def format_book(book):
    """Format a book's details into a readable string."""
    status = "Read" if book["read_status"] else "Unread"
    return (f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, "
            f"Genre: {book['genre']}, Status: {status}")

def main():
    """Main function to run the library manager."""
    global library
    library = load_library()
    
    st.title("Personal Library Manager")
    menu_options = [
        "Add a Book",
        "Remove a Book",
        "Search for a Book",
        "Display All Books",
        "Display Statistics",
        "Exit"
    ]
    choice = st.sidebar.selectbox("Menu", menu_options)
    
    if choice == "Add a Book":
        add_book()
    elif choice == "Remove a Book":
        remove_book()
    elif choice == "Search for a Book":
        search_books()
    elif choice == "Display All Books":
        display_all_books()
    elif choice == "Display Statistics":
        display_statistics()
    elif choice == "Exit":
        st.write("Exiting the program. Goodbye!")
        st.stop()

if __name__ == "__main__":
    main()