# import classes
from library_system import Book, Member, Loan

def main():
    # create a list of books to choose from
    books = [
        Book("hunger games"),
        Book("harry potter"),
        Book("the great gatsby"),
        Book("the lord of the rings")
    ]
    
    # create a member object
    member = Member("Bob")

    # list to store the active loans
    active_loans = []

    # menu
    while True:
        print("\n--- Library Menu ---")
        print("1. View books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View borrowed titles")
        print("5. Quit\n")

        choice = input("Choose an option: ")

        # 1. view books
        if choice == "1":
            for book in books:
                if not book.is_checked_out:
                    print(book.title.title(), "(Available)")
                else:
                    print(book.title.title(), "(Unavailable)")

        # 2. borrow a book 
        elif choice == "2":
            title = input("Enter the title of the book you would like to borrow: ")
            given_title = title.lower()
            for book in books:
                # check if given title is in our books
                if book.title == given_title:
                    loan = member.borrow(book) # Loan(book, self: member)
                    # loan was successful
                    if loan:
                        active_loans.append(loan)
                        print(f"{book.title.title()} was added successfully, enjoy reading!")
                    else:
                        print(f"{book.title} cannot be added it is currently unavailable")

        # 3. return a book
        elif choice == "3":
            title = input("Enter the title of the book you would like to return: ")
            given_title = title.lower()
            # for each loan check the title of the book attached to that loan 
            for loan in active_loans:
                if loan.book.title == given_title:
                    # returns the book, and updates the loan status of the book
                    if loan.close():
                        print(f"{loan.book.title.title()} was returned successfully!")
                        active_loans.remove(loan)
                    else:
                        print("No active loan found for that book")
                        
        # 4. view borrowed titles
        elif choice == "4":
            # check if member borrowed any books
            if not member.borrowed_titles:
                print("You haven't borrowed any books")
            else:
                print("--- List of borrowed books ---")
            for title in member.borrowed_titles:
                print(title.title())
    
        # 5. quit
        elif choice == "5":
            break
    
        else:
            print("Invalid please enter (1-5).")
    
main()