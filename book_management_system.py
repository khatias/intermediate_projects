from datetime import datetime

class Book:
    def __init__(self, title, author, year_of_publication):
        # Constructor for Book class
        self.title = title  
        self.author = author  
        self.year_of_publication = year_of_publication  


class BookManager:
        # Constructor for BookManager class
    def __init__(self):
    
         self.books = [
            Book("Clockwork Orange", "Anthony Burgess", 1962),
            Book("Data Tutashkhia", "Chabua Amirejibi", 1975),
            Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
        ] 

    def add_book(self, title, author, year_of_publication):
        #  add a new book to the list 
        book = Book(title, author, year_of_publication)  
        self.books.append(book)  

    def show_books(self):
        # display all books in the list
        if len(self.books) < 1:
            print("The list does not contain any books.")
        else:
            for book in self.books:
               
                print(f"Title: {book.title}, Author: {book.author}, Year of Publication: {book.year_of_publication}")

    def search_book(self, title):
        # search for a book by title
        found = False  
        for book in self.books:
            if book.title == title:
 
                print(f"Title: {book.title}, Author: {book.author}, Year of Publication: {book.year_of_publication}")
                found = True
        if not found:

            print("No books were found under this title.")


class BookManagementSystem:
    def __init__(self):
        # Constructor for BookManagementSystem class
        self.manager = BookManager()  # Create an instance of BookManager to manage books

    def display_menu(self):
        # Method to display the main menu and handle user input
        print("Welcome to the Book Management System!")
        while True:
            print("\nMenu:")
            print("1) Add a new book")
            print("2) View all books")
            print("3) Search book by title")
            print("4) Exit\n")

            try:
                option = int(input("Please make your selection: "))  # Get user input for menu option
                if option == 1:
                    self.add_book()  
                elif option == 2:
                    self.show_books()  
                elif option == 3:
                    self.search_book() 
                elif option == 4:
                    print("Exiting the application.") 
                    break
                else:
                    print("Please make a selection between 1 and 4.") 
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")  

    def add_book(self):
        # Method to add a new book
        title = input("Please enter the title of the book: ") 
        author = input("Please enter the name of the author: ")  
        while True:
            year = input("Please enter the year of publication: ")
            if not year.isdigit():
                print("Invalid input. Please enter a number for the year of publication.")
                continue
            year = int(year)
            current_year = datetime.now().year
            if year > current_year:
                print("Invalid year. Publication year cannot be in the future.")
            else:
                break
        self.manager.add_book(title, author, year)
        print("Book added.")

    def show_books(self):
        # Method to display all books
        self.manager.show_books()  

    def search_book(self):
        # Method to search for a book by title
        title = input("Please enter the title of the book: ") 
        self.manager.search_book(title) 


book_management_system = BookManagementSystem()  # Create an instance of BookManagementSystem
book_management_system.display_menu()  # Call method to display menu and handle user input
