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

rows_in=input("Input height of Pascal's triangle...")
rows=int(rows_in)
for rownum in range (rows):
    newValue=1
    PrintingList = [newValue]
    for iteration in range (rownum):
        newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
        PrintingList.append(int(newValue))
    print(PrintingList)
print()
