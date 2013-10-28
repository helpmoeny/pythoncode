def Create_Dic(Inputfile):
    fp=open(Inputfile,"r")
    county={}
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
    #for index in county:
        #print(index,county[index])
    return county

def print_data(county):
    #The format for printing a county! Actually prints the county it was given
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
    return dictionary[key]

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
    return dictionary[key]

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
            print("County: ",count_init)
            match = next(val for key, val in dictionary.items() if count_init in key.lower())
            print(match)
        except StopIteration:
            print("Not found")
    #feeds the county it found to print_data for printing

# Can print_data stay in the spot it's at in the code? Since the other functions just call upon it and feed it a county to print

county_dict=Create_Dic("est11_MI.txt")
for index in sorted(county_dict):
    print(index,county_dict[index])

print_highest_data(county_dict)
print_lowest_data(county_dict)
print_county_data(county_dict)
