value_int=input("Enter integer: ")
value=int(value_int)
if value == 0:
    print("that's too easy")
elif value < 0:
    print("sorry, no negatives")
else:
    binlist=[]
    binlistr=[]
    while True:
        binlist.append(value%2)
        quotient=value//2
        if quotient==0:
            break
        else:
            value = quotient
    binlistr=list(binlist)
    binlistr.reverse()
    print("Binary Value of ", value_int, " is",binlistr)
    decnumber = 0
    for i in range(len(binlist)):
        if binlist[i]==1: 
            decnumber+=2**i
    print("Decimal Value of ", binlistr, " is",decnumber)
