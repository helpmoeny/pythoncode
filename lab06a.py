def make_new_row(old_row):
    new_row=[1]
    pos=1
    if old_row==[]:
        print("[1]")
    elif old_row==[1]:
        print("[1,1]")
    else:
        while True:
            new_row.insert(pos,old_row[pos-1]+old_row[pos])
            if old_row[pos]==1:
                new_row.append(1)
                break
            pos+=1
        return new_row;

rows_in=input("Input height of Pascal's triangle...")
rows=int(rows_in)
old_row=[]
for rownum in range (rows):
    newrow=make_new_row(old_row)
    print(newrow)
    old_row=newrow
print()
