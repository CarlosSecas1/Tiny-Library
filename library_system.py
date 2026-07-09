class Book:
    """
    A class to represent a book.
    
    Attributes:
        title (str): The book's name
        self.is_checked_out (boolean): A boolean flag on the book object that
                                       tracks whether the book is currently borrowed
    """
    def __init__(self, title: str):
        """Initialize a new Book instance."""
        self.title = title
        self.is_checked_out = False

    def checkout(self):
        """Tries to checkout the book if it is available."""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        else:
            return False
    
    def return_book(self):
        """Return the book and marks the status to be available."""
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        else:
            return False
    
class Member:
    """
    A class to represent a Member.

    Attributes:
        name (str): The name of the member
        self.borrowed_titles (list): A list of books the member borrows
    """
    def __init__(self, name: str):
        """Initilaize a new Member instance"""
        self.name = name
        self.borrowed_titles = []
    
    def borrow(self, book: Book):
        """
        A member can borrow a book and updates the list
        of the titles of books the member is currently borrowing.

        Args:
            book (Book): The book the member wants to borrow
        """
        if book.checkout():
            self.borrowed_titles.append(book.title)
            loan = Loan(book, self)
            return loan
        else:
            return None

    def return_book(self, book: Book):
        """
        A member can return a book from their list
        of borrowed titles.

        Args:
            book (Book): the book the members wants to return
        """
        if book.return_book():
            self.borrowed_titles.remove(book.title)
            return  True
        else:
            return False
    
class Loan:
    """
    A class to represent the loan status for a book
    corresponding to a member.

    Attributes:
        book (Book): A book instance of the Book class
        member (Member): A member instance of the Member class
        self.active (boolean): A flag for updating the staus of a loan
    """
    def __init__(self, book :Book, member: Member):
        """Intialize a new Loan instance."""
        self.book = book
        self.member = member
        self.active = True
    
    def close(self):
        """
        Closes the loan by returning the borrowed book
        and marking the loan as inactive.
        """
        if self.active:
            self.member.return_book(self.book)
            self.active = False
            return True
        else:
            return False
