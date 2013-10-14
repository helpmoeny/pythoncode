
def make_new_row(old_row):
    new_row=[1]
    pos=1
    while True:
        new_row.insert(pos,old_row[pos-1]+old_row[pos])
        if old_row[pos]==1:
            new_row.append(1)
            break
        pos+=1
    return new_row;

#def make_new_row(old_row):
#    new_row=[1]
#    for i in old_row:
#         new_row.insert(i,old_row[i-1]+old_row[i])
#    new_row.append(1)
#   return new_row;

#    """Requires:
#       -- list old_row that begins and ends with a 1 and has zero or more
#          integers in between (has to have at least [1,1])
#       Returns:
#       -- list beginning and ending with a 1 and each interior (non 1)
#          integer is the sum of the corresponding old_row elements
#          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
#          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """

    
old_row=[1,1]
rows = int(input("how big "))
print ("[1]")
print(old_row)
for i in range(rows-2):
    new_row=make_new_row(old_row)
    print(new_row)
    old_row=new_row
