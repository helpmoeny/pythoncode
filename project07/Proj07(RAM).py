import string
def Create_Dic(Inputfile):
    county={}
    try:
        fp=open(Inputfile,"r")
        for line in fp:
            line_list=line.split()
            if int(line_list[1])>0:
                countyname=line_list[23]
                count=24
                while True:
                    if line_list[count].upper()!= "COUNTY":
                        countyname = countyname + " " + line_list[count]
                        count+=1
                    else:
                        break
                county_data=(line_list[8],line_list[11],line_list[20])
                if countyname in county:
                    print("Error: Duplicate County Data")
                else:
                    county[countyname]=county_data
    except IOError:
        print("cannot open that file,quitting")
        county=0
    return county

def print_data(county):
    #The format for printing a county! Actually prints the county it was given
    people_int=int(county[0])
    people=people_int
    income_int=int(county[2])
    income=income_int
    #print(name, "County")
    print('Children Ages 0-17 in Poverty'.ljust(45),(str(people).rjust(10)))
    print('Percentage of people ages 0-17 in Poverty'.ljust(45),"{:>10}%".format(str(county[1]).rjust(10)))
    print('Median household income'.ljust(45),("${:6,d}".format(income).rjust(10)))    
    print()

def print_highest_data(dictionary):
    #Finds the county with the max percentage of childern in poverty
    maxvalue=0
    key=""
    for i in dictionary:
        county_info=dictionary[i]
        if float(county_info[1])>maxvalue:
            maxvalue=float(county_info[1])
            key=i
    #returns the dictionary value for that specific key where it found the max value
    print("County with the max percentage of childern in poverty")
    print(key, "County")
    print_data(dictionary[key])

def print_lowest_data(dictionary):
    #Finds the county with the min percentage of childern in poverty and returns it
    minvalue=100
    key=""
    for i in dictionary:
        county_info=dictionary[i]
        if float(county_info[1])<minvalue:
            minvalue=float(county_info[1])
            key=i
    #returns the dictionary value for that specific key where it found the min value
    print("County with the min percentage of childern in poverty")
    print(key, "County")
    print_data(dictionary[key])

def print_county_data(dictionary):
    #Continuously prompts for a county and then searches for it, not case sensitive and does not include the actual word county in search
    while True:
        try:
            count_init=input("Input county name to search for: ")
            count_init=count_init.lower()
            #Quit loop when q or Q is entered
            if count_init == 'q':
                print("Quiting")
                break
            match = next(val for key, val in dictionary.items() if count_init == key.lower())
            found_key=[k for k, v in dictionary.items() if v == match]
            print("County: ",str(found_key).strip(string.punctuation))
            print_data(match)
            #feeds the county it found to print_data for printing
        except StopIteration:
            print("Not found")


county_dict=Create_Dic("est11_MI.txt")
if county_dict !=0:
    #Code for looping through complete county dictionary, for viewing
    #for index in sorted(county_dict):
        #print(index,county_dict[index])
    print_highest_data(county_dict)
    print_lowest_data(county_dict)
    print_county_data(county_dict)
