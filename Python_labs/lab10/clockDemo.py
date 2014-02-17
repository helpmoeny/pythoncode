import clock

def main():
    A = clock.Time(12,13,13)#initiates A to a time

    print("Readable Time: ")
    print(repr(A))#prints human readable/official version of time
    print()
    print("Simple Time: ")
    print(str(A))#Prints Simple time
    print()
    print("New Time: ")
    A.from_str("12:12:12")#change current time
    print(A)#Prints Time (which has been changed)
    

main()
