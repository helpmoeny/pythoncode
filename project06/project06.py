def prompt_user():
    while True:
        try:
            print("What would you like to do?")
            print("1: Look up year range")
            print("2: Look up month/year")
            print("3: Search for author")
            print("4: Search for title")
            print("Q: Quit")
            userintput=input(">")
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
            if count>10:
                break
            count+=1
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
    except IOError:
        print ("Cannot open.  Try again...")
    return all_list

def search_by_title(all_list):
    t=input("Enter a title (or part of a title): ")
    for book in all_list:
        if t in book[0]:
            print(book)

def get_year(all_list):
    #Their should be no prompt, given this is used in in display_books_by_year and display_books_by_month_year
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

