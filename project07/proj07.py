#Going to setup functions and expain my logic of the proj07
#http://www.cse.msu.edu/~cse231/Projects/Project07/project07.pdf

def Create_Dic(Inputfile)
    #open the file, given from input(doesn't prompt)
    #create dictionary
    #loop through and strip lines, add to dictionay
    #set key to be the name of the county, disinclude the actual word county
    #county=line[] #strip()
    #if count in D:
        #print('error')
    #else:
        #D[count]=(....tuple...) * this checks to see if the county is already in the dictionary
    #returns dictionary

def print_data(#county)
    #The format for printing a county! Actually prints the county it was given


def print_highest_data(dictionary)
    #Finds the county with the max percentage of childern in poverty
    #feeds the county it found to print_data for printing


def print_lowest_data(dictionary)
    #Finds the county with the min percentage of childern in poverty and returns it
    #feeds the county it found to print_data for printing


def print_county_data(dictionary)
    #Continuously prompts for a county and then searches for it, not case sensitive and does not include the actual word county in search
    #Quit loop when q or Q is entered
    #feeds the county it found to print_data for printing


# Can print_data stay in the spot it's at in the code? Since the other functions just call upon it and feed it a county to print

Create_Dic(Inputfile)
print_highest_data(dictionary)
print_lowest_data(dictionary)
print_county_data(dictionary)


# keep in mind
print("{:16,d}".format(12345))
prints:(12,345)
