def get_crater_tuple(line_str):
    line_list=[]
    for item in line_str.split('\t'):
        line_list.append(item)
        #print(line_list)
    t=(line_list[0],line_list[1],line_list[2],line_list[3],line_list[4])
    return(t)

def read_craters(filename):
    while True:
        try:
            fp=open(filename)
            line_list=[]
            for line in open(filename,'r').readlines():
                line_list.append(get_crater_tuple(line))
            break
        except IOError:
            print("cannot open that file")
            print()
            filename=input("Enter a filename: ")
    fp.close()
    return line_list[3:]

def get_eligible_craters(crater_list):
    checker=True
    eligible_crater_list=[]
    for crater_tuple in crater_list:
        crater_good=True
        if float(crater_tuple[2])< -40:
            crater_good=False
        if float(crater_tuple[2])> 50:
            crater_good=False
        if float(crater_tuple[3])< 40:
            crater_good=False
        if float(crater_tuple[3])> 135:
            crater_good=False
        if float(crater_tuple[4])< 60:
            crater_good=False
        if crater_good==True:
            eligible_crater_list.append(crater_tuple)
    return eligible_crater_list;

def write_craters(eligible_crater_list):
    fo=open("craters.txt","w")
    fo.write(" ID       Name       Latitude Longitude  Diameter\n")
    for item in eligible_crater_list:
        fo.write(item[0].rjust(3)+" "+item[1].ljust(15)+" "+"{0:.2f}".format(float(item[2])).rjust(9)+" "+"{0:.2f}".format(float(item[3])).rjust(9)+" "+"{0:.2f}".format(float(item[4])).rjust(9)+"\n")
    fo.close()


filename = input("Enter a filename: ")
crater_list = read_craters(filename)
eligible_crater_list = get_eligible_craters(crater_list)
write_craters(eligible_crater_list)
