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
        count=0
        for line in fp:
            book=line.split('\t')
            all_list.append(book)
            if count>10:
                print(all_list)
                break
            count+=1
        fp.close()
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except IOError:
        print ("Cannot open.  Try again...")
    except FileNotFoundError:
        print ("File not found.  Try again...")
    return all_list

def get_month(all_list):
    month=input("Enter month (as a number, 1-12): ")
    for year in all_list:
        if t in year[:1]:
            print(year)

def display_books_by_year(library):
    begin_str=input("Enter beginning year: ")
    begin=int(begin_str)
    end_str=input("Enter ending year: ")
    end=int(end_str)
    for book in library:
        year_str=book[3]
        year_str2=year_str[:4]
        year=int(year_str2)
        if year>=end and year<=begin:
            print(book)

def display_books_by_month_year(library):
    t=input("Enter a title (or part of a title): ")
    for book in library:
        if t in book[0]:
            print(book)

def search_by_author(library):
    t=input("Enter a author's name (or part of a name): ")
    for book in library:
        if t in book[1]:
            print(book)

def search_by_title(library):
    t=input("Enter a title (or part of a title): ")
    for book in library:
        if t in book[0]:
            print(book)

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
