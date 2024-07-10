#Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list.#

def add_book(library):
    book_title=input("What book would you like to add: ")
    found=[book for book in library if book[0].lower()==book_title.lower()]
    if found:
        for book in found:
            print("Book already exist")
    else:
        author=input("Who is the Author: ")
        library.append((book_title,author))
            
def display_book(library):
    print (f"Books in library are: {library}")
            
def  main():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    while True:
        print("\nWelcome to the Library System")
        print("1: Add New Book: ")
        print("2: Display list of all books and Authors")
        print("3:  Exit")
        choice =input("Please make a selection: ")
        if choice=="1":
            add_book(library)
        elif choice=="2":
            display_book(library)
        elif choice =="3":
            print("Goodbye")
            break
        else:
            print("Invalid entry please try again")

main()
        
        
        