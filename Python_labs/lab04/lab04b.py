file_str = input("Enter a file to open: ")
total_count_int=0 #create variable to hold the count
ones=0
twoes=0
threes=0
fours=0
fives=0
sixes=0
sevens=0
eights=0
nines=0

while True:
    try:
        file_obj = open(file_str, 'r') #open file for reading
        print("Opened the file", file_str)
        break
    except IOError:
        print("Bad file name, try again")
        file_str = input("Enter a file to open: ")
    print("next iteration")

while True:
    try:
        line=file_obj.readline()
        numeral=int(line.strip()[0])
        if numeral==1:
            ones+=1
        elif numeral==2:
            twoes+=1
        elif numeral==3:
            threes+=1
        elif numeral==4:
            fours+=1
        elif numeral==5:
            fives+=1
        elif numeral==6:
            sixes+=1
        elif numeral==7:
            sevens+=1
        elif numeral==8:
            eights+=1
        elif numeral==9:
            nines+=1
        total_count_int+=1
    except IndexError:
        break

print("Digit Percent Benford")
print("    1:  %.1f" % (ones/total_count_int*100)  ," (30.1%)")
print("    2:  %.1f" % (twoes/total_count_int*100) ," (17.6%)")
print("    3:  %.1f" % (threes/total_count_int*100)," (12.5%)")
print("    4:   %.1f" % (fours/total_count_int*100) ,"  (9.7%)")
print("    5:   %.1f" % (fives/total_count_int*100) ,"  (7.9%)")
print("    6:   %.1f" % (sixes/total_count_int*100) ,"  (6.7%)")
print("    7:   %.1f" % (sevens/total_count_int*100),"  (5.8%)")
print("    8:   %.1f" % (eights/total_count_int*100),"  (4.1%)")
print("    9:   %.1f" % (nines/total_count_int*100) ,"  (4.6%)")

        
# close file
file_obj.close()

