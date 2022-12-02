# import tkinter
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()

# create global list
global catalog 
# import Book class
from Book import Book
catalog = [Book("0553296981", "The Diary of a Young Girl", "Frank, Anne", "16.50"), Book("1400082773", "Dreams from My Father", "Obama, Barrack", "24.99")]

# check ISBN valid or not
def isISBNValid(isbn):
    # check for length - this program only consider 10 digital number or 9 digital number plus "X" ISBN
    if len(isbn) != 10:
        print("\nError: Need 10 digital number or 9 digital number plus 'X' ISBN\n")
    else:    
        # strating to calculate ISBN
        sum = 0

        # step 1 : calculate first 9 digital
        for i in range(9):
            # check if the input value can be tranfer to int
            # and catch any other error
            try:
                int(isbn[i])
            except ValueError:
                # use print to know all the improper value
                print(f"Error: {isbn[i]} - ISBN input value is improper\n")
            except:
                print(f"Error: {isbn[i]} - Something else went wrong\n")
            else:                    
                # calculate int 0 to 9       
                if 0 <= int(isbn[i]) <= 9:
                    sum = sum + int(isbn[i]) * (10 - i)
                else:
                    print("Error: First 9 character need to be digital number\n")
    
        # step 2: check the last character     
        if (isbn[9] == "X"):
            # if last character is "X", add to sum.
            sum = sum + 10
        else:
            try:
                int(isbn[9])
            except ValueError:
                # use print to know all the improper value
                print(f"Error: {isbn[9]} - ISBN input value is improper\n")
            except:
                print(f"Error: {isbn[9]} - Something else went wrong\n")
            else:
                # if last chractor is int, add to sum.
                if int(isbn[9]):
                    sum = sum + int(isbn[9])
                else:
                    print("Error: Last character need to be digital number or capital 'X'\n")
    
        # step 3: divide sum by 11
        if sum % 11 == 0:
            return True
        else:
            print("Error: Invalid ISBN\n")


# Make sure user input is not empty
def checkUserInput(name, string, type):
    # if type is string, it means the input should be string type
    if type == "string":
        while True:
            name = simpledialog.askstring(title="Book Catalog", prompt=string)
            # if: any information in user input is empty
            # tell user error and let user try again
            if name == "":
                messagebox.showwarning(title = "Error", message="Input cannot be empty")
            else:
                return name

    # elif type is float, it means the input should be float type
    elif type == "float":
        while True:
            name = simpledialog.askfloat(title="Book Catalog", prompt=string)
            # if: any information in user input is empty
            # tell user error and let user try again
            if name == "":
                messagebox.showwarning(title = "Error", message="Input cannot be empty")
            else:
                return name

    # elif type is int, it means the input should be int type
    elif type == "int":
        while True:
            name = simpledialog.askinteger(title="Book Catalog", prompt=string)
            # if: any information in user input is empty
            # tell user error and let user try again
            if name == "":
                messagebox.showwarning(title = "Error", message="Input cannot be empty")
            else:
                return name


# option 1 : Add a book 
def addBook():
    # initialize variable
    isbn = ""
    title = ""
    author = ""
    price = ""

    # the user input dialog
    # check ISBN valid or not
    isbn = checkUserInput(isbn, "Enter ISBN:", "string")
    title = checkUserInput(title, "Enter title:", "string")
    author = checkUserInput(author, "Enter author:", "string")
    price = checkUserInput(price, "Enter price:", "float")

    # check user input is none or not
    # if: any information in user input is none, tell user add new book unsuccessful 
    if (isbn is None) or (title is None) or (author is None) or (price is None):
        print("\nAdding new book unsuccessful\n")

    # elif: ISBN is invalid, tell user ISBN is invalid and add new book unsuccessful
    elif (isISBNValid(isbn) != True):
        print("\nAdding new book unsuccessful\n")

    # elif: ISBN exists, tell user this ISBN exists and add new book unsuccessful
    elif(any(item for item in catalog if isbn == item.isbn)):
        print("\nThis ISBN exists, adding new book unsuccessful\n")

    # else: add the new book to catalogue 
    else:
        # create new book object
        newBook = Book(isbn, title, author, price)
        # add the new book to the catalog list
        catalog.append(newBook)
        messagebox.showinfo("Add a Book", "Adding book successfully")


# option 2 ： Sort and display books by price
def sortBooks():
    # check catalog 
    # if catalog is empty, tell user there are no books
    if len(catalog) == 0:
        messagebox.showwarning(title = "Display All Books", message="There are no books in the catalog")
    # else: sort and display books by price
    else:
        # sort by price
        catalog.sort(key=lambda item: item.price)

        # display all books
        bookString = ""

        for item in catalog:
            bookString += item.__str__()
        
        messagebox.showinfo(message=bookString)


# option 3 : Search for a book by title
def searchByTitle():
    # check catalog 
    # if catalog is empty, tell user there are no books
    if len(catalog) == 0:
        messagebox.showwarning(title = "Display All Books", message="There are no books in the catalog")
    # else: find and display book
    else:
        # create book information string
        bookString = ""

        # take user input 
        title = ""
        title = checkUserInput(title, "Enter title to search:", "string")

        # check user input is none or not
        # if: information in user input is none, tell user search book unsuccessful
        # else: search book by title 
        if (title is None):
            print("\nSearching book unsuccessful\n")
        else:
            # find the book by title
            for item in catalog:
                if title in item.title:
                    bookString += item.__str__()
        
            # display in dialog
            if bookString == "":
                messagebox.showinfo(message="Sorry, we didn't fint your book.")
            else:
                messagebox.showinfo(message=bookString)
          

# option 4 : Delete a book
def deleteBook():
    # take user input
    isbn = ""
    isbn = checkUserInput(isbn, "Enter ISBN to search:", "string")

    # check user input is none or not
    # if: information in user input is none, tell user delete book unsuccessful
    # else: delete the book
    if (isbn is None):
        print("Delete book unsuccessful\n")
    else:
        # create book information string
        bookString = ""

        # check the ISBN is in catalog or not
        for item in catalog:
            if isbn == item.isbn:
                # find the book
                # create a variable to store the found book
                foundBook = item
                bookString = item.__str__()
                confirmString = bookString + "\n Are you sure you want to delete this book?"                
            # else: doesn't find the book


        # display dialog
        if bookString == "":
            messagebox.showinfo(message="Doesn't find the book")
        else:
            # ask for confirmation
            response = messagebox.askquestion("Confirmation", confirmString)
            if response == "yes":
                # delete the book
                catalog.remove(foundBook)
                messagebox.showinfo("Confirmation", "Book HAS been deleted")                

            elif response == "no":
                messagebox.showinfo("Confirmation", "Book has NOT been deleted")
            else:
                messagebox.showwarning("Error", "Something went wrong")

            # reset bookstring
            bookString = ""


# option 5 ： Display all books
def displayAllBooks():
    # check catalog 
    # if catalog is empty, tell user there are no books
    if len(catalog) == 0:
        messagebox.showwarning(title = "Display All Books", message="There are no books in the catalog")
    # else: display books 
    else:
        # create string variable to store book information
        bookString = ""

        for item in catalog:
            bookString += item.__str__()
        
        # display in dialog
        messagebox.showinfo(message=bookString)


# option 6 ： Exit
def exitProgram():
    # create exit string for dialog
    exit = "Exit book catalog?"

    # ask for confirmation
    response = messagebox.askquestion("Confirmation", exit)
    if response == "yes":
        messagebox.showinfo("Confirmation", "Bye")
        return True
    elif response == "no":
        messagebox.showinfo("Confirmation", "NOT exit")
    else:
        messagebox.showwarning("Error", "Something went wrong")


# create book menu system
def menuSystem():
    
    # create string to store dialog display message
    displayString = ""
    displayString += "--Holmesglen Book Store--\n"
    displayString += "\n1. Add a book\n"
    displayString += "2. Sort and display books by price\n"
    displayString += "3. Search for a book by title\n"
    displayString += "4. Delete a book\n"
    displayString += "5. Display all books\n"
    displayString += "6. Exit\n"
    displayString += "\nEnter menu choice"

    # if exitApp is false, can stay in book catalog program as long as user want to
    # if exitApp is True, close the catalog program without confirmation.
    exitApp = False

    # display dialog and get user input
    while exitApp == False  :

        # make sure user input is int type and not empty
        choice = simpledialog.askinteger("Book Catalog", displayString)

        # check input validation
        # if: input is None (click cancel button or cross button), exit program without confirmation
        if choice is None:
            exitApp = True

        # elif: input is int between 1 to 6, run the chosen option
        elif (1 <= choice <= 6):
            match choice:
                # option 1: Add a book
                case 1:
                    addBook()
                
                # option 2 : Sort and display books by price
                case 2:
                    sortBooks()
                
                # option 3 : Search for a book by title
                case 3:
                    searchByTitle()

                # option 4 : Delete a book
                case 4:
                    deleteBook()

                # option 5 : Display all books
                case 5:
                    displayAllBooks()
                
                # option 6 : Exit
                case 6:
                    response = exitProgram()  
                    if response == True:
                        exitApp = True     

        # else: input is int type but not between 1 to 6, tell user it is invalid input and bring user back to menu
        else:
            # invalid input 
            messagebox.showinfo("Invalid Input", "Please enter options 1 - 5\n\nIf want to exit, enter 6")
        

# call menu system - Book Catalog
menuSystem()