def prompt_user():
    while True:
        try:
            print("What would you like to do?")
            print("1: Look up year range")
            print("2: Look up month/year")
            print("3: Search for author")
            print("4: Search for title")
            print("Q: Quit")
            userinput=input(">")
            #fp=open(userint)
            #How to vailidate possibility of opening file to prompt correct errors
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
        except IOError:
            print ("Cannot open.  Try again...")
        return userinput

def get_books():
    try:
        fp=open('bestsellers.txt')
        all_list=[]
        count=0
        for line in fp:
            book=line.split('\t')
            all_list.append(book)
            #How to remove last element of list, i've tried several times ugh!
            #all_list.pop() #this function doesn't work because it returns that last value
            if count>10:#***for now I'm testing the first 10 lines of text file, but i've noticed some problems***
                print(all_list)
                print(book)
                break
            count+=1
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except IOError:
        print ("Cannot open.  Try again...")
    fp.close()
    return all_list

def get_year(all_list):
    #Their should be no prompt, given this is used in display_books_by_year and display_books_by_month_year
    begin=input("Enter beginning year: ")
    end=input("Enter ending year: ")
    for year in all_list:
        if t in year[:1]:
            print(year)
    

def get_month(all_list):
    month=input("Enter month (as a number, 1-12): ")
    for year in all_list:
        if t in year[:1]:
            print(year)

#I Don't understand get_text at ALL, seems like it would over complicate things...
#IGNORE BELOW: HAVN"T DEFINED FUNCTIONS YET! (Except search_by_title)

def display_books_by_year():
    t=input("Enter a title (or part of a title): ")
    for book in all_list:
        if t in book[0]:
            print(book)

def display_books_by_month_year():
    t=input("Enter a title (or part of a title): ")
    for book in all_list:
        if t in book[0]:
            print(book)

def search_by_author():
    t=input("Enter a title (or part of a title): ")
    for book in all_list:
        if t in book[0]:
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
        display_books_by_year()
    if selection=='2':
        display_books_by_month_year()
    if selection=='3':
        search_by_author()
    if selection=='4':
        search_by_title(library)
    if selection=="Q":
        print("Thank you and have a nice day")
        break
