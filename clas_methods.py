# Assignment No: 11

# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        # print(f"Total books: {cls.total_books}")
        # return cls.total_books
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("Pride and Prejudice", "Jane Austen")
book5 = Book("The Catcher in the Rye", "J.D. Salinger")
book6 = Book("The Hobbit", "J.R.R. Tolkien")
book7 = Book("Fahrenheit 451", "Ray Bradbury")
book8 = Book("Brave New World", "Aldous Huxley")
book9 = Book("The Picture of Dorian Gray", "Oscar Wilde")
book10 = Book("The Alchemist", "Paulo Coelho")

print(f"Total books created: {Book.total_books}")