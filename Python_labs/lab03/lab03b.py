value_int=input("Enter integer: ")
value=int(value_int)
if value<0:
    print("Don't enter negative numbers!")
elif value==0:
    print("Terminate")
else:
    binlist=[]
    while True:
        binlist.append(value%2)
        quotient=value//2
        if (quotient==0):
            break #when quotient equals zero, we break out of the while loop
        else:
            value = quotient

    binlist.reverse()
    print(binlist)
    binlist.reverse()

    power=0
    equal=0
    for power in range(len(binlist)):
        if binlist[power]==1:
            equal+=2**power
            power+=1
        else:
            power+=1
    print(equal)
