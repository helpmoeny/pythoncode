import clock

def main():
    A = clock.Time(12,13,13)#initiates A to a time
    print( A )#Print time
    A.from_str("12:12:12")#change current time AND PRINT
    print()

main()
