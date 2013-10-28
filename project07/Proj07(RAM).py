#Going to setup functions and expain my logic of the proj07
#http://www.cse.msu.edu/~cse231/Projects/Project07/project07.pdf

def Create_Dic(Inputfile):
    #open the file, given from input(doesn't prompt)
    fp=open(Inputfile,"r")
    county_dict={}
    for line in fp:
        line_list=line.split()
        if int(line_list[1])>0:
            county=line_list[23]
            count=24
            while True:
                if line_list[count].upper()!= "COUNTY":
                    county = county + " " + line_list[count]
                    count+=1
                else:
                    break
            county_data=(line_list[8],line_list[11],line_list[20])
            if county in county_dict:
                print("Error: Duplicate County Data for ", county, " county ignored.")
            else:
                county_dict[county]=county_data
    fp.close()
    return county_dict

def print_data(county):
    #The format for printing a county! Actually prints the county it was given
    print()
    
def print_highest_data(dictionary):
    #Finds the county with the max percentage of childern in poverty
    #feeds the county it found to print_data for printing
    print()
def print_lowest_data(dictionary):
    #Finds the county with the min percentage of childern in poverty and returns it
    #feeds the county it found to print_data for printing
    print()
def print_county_data(dictionary):
    #Continuously prompts for a county and then searches for it, not case sensitive and does not include the actual word county in search
    #Quit loop when q or Q is entered
    #feeds the county it found to print_data for printing
    print()

# Can print_data stay in the spot it's at in the code? Since the other functions just call upon it and feed it a county to print

county_dict=Create_Dic("est11_MI.txt")
for index in sorted(county_dict):
    print(index,county_dict[index])

print_highest_data(county_dict)
print_lowest_data(county_dict)
print_county_data(county_dict)


# keep in mind
#print("{:16,d}".format(12345))
#prints:(12,345)
