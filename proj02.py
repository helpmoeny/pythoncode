#code=input("Enter customer code:")
while True:
    print("")
    code=input("Enter customer code:")
    bill_float = 0
    bill = float(bill_float)
    if code == "r":
        begin_int=input("Enter beginning meter reading:")
        begin = float(begin_int)
        end_int=input("Enter ending meter reading:")
        end = float(end_int)
        Used = .1*(end-begin)
        Used_rounded = round(Used,2)
        bill = 5.00+ .0005*Used
        bill_rounded = round(bill,2)
        print("")
        print("Customer code: ",code)
        print("Beginning meter reading: ",begin_int)
        print("Ending meter reading:    ",end_int)
        print("Gallons of water used: ",Used_rounded)
        print("Amount billed: $",bill_rounded)
    elif code == "c":
        begin_int=input("Enter beginning meter reading:")
        begin = float(begin_int)
        end_int=input("Enter ending meter reading:")
        end = float(end_int)
        if end<begin:
            Used = .1*((1000000000-begin)+end)
        else:
            Used = .1*(end-begin)
        if Used <= 4000000.00:
            bill = 1000.00
        elif Used >4000000.00:
            bill = 1000.00+.00025*Used
        else:
            print("broken")
        Used_rounded = round(Used,2)
        bill_rounded = round(bill,2)
        print("")
        print("Customer code: ",code)
        print("Beginning meter reading: ",begin_int)
        print("Ending meter reading:    ",end_int)
        print("Gallons of water used: ",Used_rounded)
        print("Amount billed: $",bill_rounded)
    elif code == "i":
        begin_int=input("Enter beginning meter reading:")
        begin = float(begin_int)
        end_int=input("Enter ending meter reading:")
        end = float(end_int)
        if end<begin:
            Used = .1*((1000000000-begin)+end)
        else:
            Used = .1*(end-begin)
        if Used <= 4000000.00:
            bill = 1000.00
        elif 4000000< Used <= 10000000.00:
            bill = 2000.00
        elif Used > 10000000.00:
            bill = 2000.00+.00025*Used
        else:
            print("broken")
        Used_rounded = round(Used,2)
        bill_rounded = round(bill,2)
        print("")
        print("Customer code: ",code)
        print("Beginning meter reading: ",begin_int)
        print("Ending meter reading:    ",end_int)
        print("Gallons of water used: ",Used_rounded)
        print("Amount billed: $",bill_rounded)
    elif code == "zz":
       print("Terminating")
       break
    else:
        print("Please input a correct code character(i,r,c) Or(zz) to terminate")
