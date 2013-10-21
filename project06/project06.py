def prompt_user():
    print("What would you like to do?")
    print("1: Look up year range")
    print("2: Look up month/year")
    print("3: Search for author")
    print("4: Search for title")
    print("Q: Quit")
    userinput=input(">")
    return userinput

def get_books():
    try:
        fp=open('bestsellers.txt')
        all_list=[]
        for line in fp:
            book=line.split('\t')
            all_list.append(book)
        fp.close()
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except IOError:
        print ("Cannot open.  Try again...")
    except FileNotFoundError:
        print ("File not found.  Try again...")
    return all_list

def print_book(book):
    print('{}, by {} {}'.format(book[0], book[1], book[3]))

def display_books_by_year(library):
    while True:
        try:
            begin_str=input("Enter beginning year: ")
            begin=int(begin_str)
            end_str=input("Enter ending year: ")
            end=int(end_str)
            break
        except:
            print("Invalid input")
    for book in library:
        year_str=book[3]
        year_str2=year_str[-4:]
        year=int(year_str2)
        if year<=end and year>=begin:
            print_book(book)
        

def display_books_by_month_year(library):
    month=input("Enter month (as a number, 1-12): ")
    t=input("Enter year: ")
    for book in library:
        date_str=book[3]
        date=date_str.split('/')
        month_int=int(date[1])
        year=int(date[2])
        if year==int(t) and int(month)==month_int:
            print_book(book)

def search_by_author(library):
    t=input("Enter a author's name (or part of a name): ")
    for book in library:
        if t in book[1]:
            print_book(book)

def search_by_title(library):
    t=input("Enter a title (or part of a title): ")
    for book in library:
        if t in book[0]:
            print_book(book)

while True:
    library=get_books() #Made the library from the list returned by get_books
    selection=prompt_user()
    if selection=='1':
        display_books_by_year(library)
    if selection=='2':
        display_books_by_month_year(library)
    if selection=='3':
        search_by_author(library)
    if selection=='4':
        search_by_title(library)
    if selection=="Q":
        print("Thank you and have a nice day")
        break
