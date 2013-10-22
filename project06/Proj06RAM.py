def prompt_user(): #Get user selection and return
    print("")
    print("What would you like to do?")
    print("1: Look up year range")
    print("2: Look up month/year")
    print("3: Search for author")
    print("4: Search for title")
    print("Q: Quit")
    userinput=input(">")
    return userinput

def get_books():# Read and process input file. return list
    all_list=[]
    try:
        fp=open('bestsellers.txt')
        for line in fp:
            book=line.split('\t')
            all_list.append(book)
        fp.close()
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except IOError:
        print ("Cannot open good bye...")
    except FileNotFoundError:
        print ("File not found try again...")
    return all_list

def print_book(book): #print single book, formatted
    print(' {}, by {} {}'.format(book[0].strip(), book[1].strip(), book[3].strip()))

def display_books_by_year(library):# find and display books by year
    while True:
        try:
            begin_str=input("Enter beginning year: ")#Negative years are legit
            begin=int(begin_str)
            end_str=input("Enter ending year: ")#Negative years are legit
            end=int(end_str)
            if begin>end:
                raise ValueError
            break
        except:
            print("Invalid input")
    foundone=False
    print("")
    print("All Titles between ",begin," and ",end)
    for book in library:
        year_str=book[3].strip()
        year_str2=year_str[-4:]
        year=int(year_str2)
        if year<=end and year>=begin:
            print_book(book)
            foundone=True
    if foundone==False:
        print("Didn't find book with search")
        

def display_books_by_month_year(library): #Find and display books by month & year
    while True:
        month=input("Enter month (as a number, 1-12): ")
        if int(month)<1 or int(month)>12:
            print("invalid input")
        else:
            break
    t=input("Enter year: ")#Negative years are legit
    foundone=False
    print("")
    print("All Titles in month ",month," of ",t)
    for book in library:
        date_str=book[3].strip()
        date=date_str.split('/')
        month_int=int(date[0])
        year=int(date[2])
        if year==int(t) and int(month)==month_int:
            print_book(book)
            foundone=True
    if foundone==False:
        print("Didn't find book with search")

def search_by_author(library): #Find and display books by Author
    t=input("Enter a author's name (or part of a name): ")
    foundone=False
    for book in library:
        if t.upper() in book[1].upper():
            print_book(book)
            foundone=True
    if foundone==False:
        print("Didn't find book with search")

def search_by_title(library): #Finde and display books by Title
    t=input("Enter a title (or part of a title): ")
    foundone=False
    for book in library:
        if t.upper() in book[0].upper():
            print_book(book)
            foundone=True
    if foundone==False:
        print("Didn't find book with search")

while True: #Main loop
    library=get_books() #Made the library from the list returned by get_books
    if len(library)==0: #Library processing failed
        break
    else:
        selection=prompt_user()
        if selection=='1':
            display_books_by_year(library)
        elif selection=='2':
            display_books_by_month_year(library)
        elif selection=='3':
            search_by_author(library)
        elif selection=='4':
            search_by_title(library)
        elif selection=="Q" or selection=="q":
            print("Thank you and have a nice day")
            break
        else:
            print("Invalid input. Please try again.")
