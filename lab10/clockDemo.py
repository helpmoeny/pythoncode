import clock

def main():
    A = clock.Time(12,13,13)#initiates A to a time

    print("Readable Time: ")
    print(A.__repr__())#prints human readable version of time
    print()
    print("Watch Time: ")
    print(A.__str__())#Prints time
    print()
    print("New Time: ")
    A.from_str("12:12:12")#change current time AND PRINT
    print()

main()
