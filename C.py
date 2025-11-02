def show_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Users")
    print("6. Show Genre Graph")
    print("7. Search Book")
    print("8. Delete Book")
    print("9. Exit")
def add_book(): 
    book_id = input("Book ID: ")
    if book_id in library:
        print("Book already exists.")
        return
    title = input("Book Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    library[book_id] = {
        "title": title,
        "author": author,
        "genre": genre,
        "issued": False
    }
    print("Book added!")
def view_books():
    if len(library) == 0:
        print("No books available.")
        return
    for book_id in library:
        book = library[book_id]
        status = "Issued" if book["issued"] else "Available"
        print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {status}")

def issue_book():
    user = input("User Name: ")
    book_id = input("Book ID to issue: ")
    if book_id not in library:
        print("Book not found.")
        return
    if library[book_id]["issued"]:
        print("Book is already issued.")
        return
    library[book_id]["issued"] = True
    if user not in users:
        users[user] = []
    users[user].append(book_id)
    print("Book issued!")

def return_book():
    user = input("User Name: ")
    book_id = input("Book ID to return: ")
    if user in users and book_id in users[user]:
        users[user].remove(book_id)
        library[book_id]["issued"] = False
        print("Book returned!")
    else:
        print("Invalid user or book.")

def view_users():
    if len(users) == 0:
        print("No users.")
        return
    for user, books in users.items():
        print(f"{user} has books: {' '.join(books)}")
def show_genre_graph():
    genres = {}
    for book in library.values():
        genre = book["genre"]
        genres[genre] = genres.get(genre, 0) + 1
    if len(genres) == 0:
        print("No data for graph.")
        return
    labels, values = genres.keys(), genres.values()
    plt.bar(labels, values, color='lightgreen')
    plt.title('Books by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Books')
    plt.show()
def search_book():
    keyword = input("Enter title, author, or genre to search: ")
    found = False
    for book_id, book in library.items():
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower() or keyword.lower() in book["genre"].lower():
            print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
            found = True
    if not found:
        print("No matching books found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in library:
        del library[book_id]
        for user in users:
            if book_id in users[user]:
                users[user].remove(book_id)
        print("Book deleted.")
    else:
        print("Book not found.")
def save_data():
    try:
        with open("library.txt", "w") as f:
            for book_id, book in library.items():
                line = f"{book_id},{book['title']},{book['author']},{book['genre']},{book['issued']}\n"
                f.write(line)
        with open("users.txt", "w") as f:
            for user, books in users.items():
                f.write(f"{user}:{','.join(books)}\n")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    while True:
        show_menu()
        choice = input("Your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_users()
        elif choice == "6":
            show_genre_graph()
        elif choice == "7":
            search_book()
        elif choice == "8":
            delete_book()
        elif choice == "9":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Wrong choice, try again.")
main()
