def displayBook():
    print("Books present in the library: ")
    for book in listOfBooks:
        print("*"+ book)

def issueBook():
    issuerName = input("Enter your name: ")
    issueBookName = input("Enter your book name you watn to issue: ")
    listOfBooks.remove(issueBookName)
    with open("Issue books record.txt","a") as f1:
        f1.write(issuerName+"\t"+issueBookName+"\n")
    print(f"{issueBookName} is issue in your name. So, handle carefully and return within 30 days.")

def returnBook():
    returnerName = input("Enter your name: ")
    returnBookName = input("Enter your book name which you want to return: ")
    listOfBooks.append(returnBookName)
    with open("Return books record.txt","a") as f2:
        f2.write(returnerName+"\t"+returnBookName+"\n")
    print("I hope you enjoyed this book.")
    return returnBookName

def greet():
    print("Thank you for visiting KVS Library. Visit Again")

try:
    listOfBooks = ['Python','Java','HTML','CSS','JavaScript','PHP']
    while True:
        print('''======Welcome to KVS Library======
        Please choose correct option: 
            1. Display all books present in the library.
            2. Request/Issue book.
            3. Return book.
            4. Exit.
        ''')
        a = int(input("Enter your choice: "))

        if a == 1:
            displayBook()
        elif a == 2:
            issueBook()
        elif a == 3:
            returnBook()
        elif a == 4:
            greet()
            break
        else:
            print("Please enter correct option.")
except ValueError:
    print("This book is issued to someone else.")