from math import exp, expm1
import os
#define variables:

#define functions:
def get_number(one_line):
    return one_line[:6]
def get_balance(one_line):
    bal=float(one_line[7:17])
    return bal
def get_name(one_line):
    return one_line[18:]
def equal_floats(x_flt,y_flt):
    equal=abs(x_flt-y_flt)
    if equal < expm1(1e-8):
        return True
    else:
        return False

#open the input & output files
file_str=input("Enter a file name: ")
filename_in=file_str+".old.txt"
filenew=file_str+".new.txt"


#deal with any file errors
try:
    fi=open(filename_in,"r")
except IOError:
    print("Input file cannot be opened...")
    os._exit(1)
try:
    fo=open(filenew,"w")
except IOError:
    print("Output file cannot be opened...")
    os._exit(1)
    
for one_line in fi:
    account_nr = get_number(one_line)
    if account_nr == "999999":
        break
    else:
        name= get_name(one_line)
        balance = float(get_balance(one_line))
    while True:
        print("Current Customer Information")
        print("Account ",account_nr)
        print("Balance $", balance)
        print("Name ", name)
        trans=input("Enter a command (a,c,d,w): ")#Prompt for transaction
        if trans == "d":
            deposit_in=input("Deposit amount: ")#prompt for deposit amount
            try:
                deposit=float(deposit_in)
                if deposit < 0:
                    print("******Do not input negative numbers try again...******")
                    print("")
                elif deposit+balance > 9999999.99:#check input for errors
                    print("******Can't Deposit that much******")
                    print("")
                else:
                    balance = balance + deposit
            except ValueError:
                print("******Incorrect input, try again******")
                print("")
        elif trans == "w":
            withdrawl_in=input("Withdrawl amount: ")#prompt for withdrawl amount
            try:
                withdrawl=float(withdrawl_in)
                if withdrawl < 0:
                    print("******Do not input negative numbers try again...******")
                    print("")
                elif withdrawl > balance: #check input for errors
                    print("******Can't withdraw that much******")
                    print("")
                else:
                    balance = balance - withdrawl
            except ValueError:
                print("******Incorrect input, try again******")
                print("")
        elif trans == "a":
            out_line=account_nr+" "+ str("{0:.2f}".format(balance)).rjust(10)+ " "+name
            fo.write(out_line)
            #go to next record
            break
        elif trans == "c":
            if equal_floats(0,balance)==True:
                print("******Account closed, moving on...******")#display invalid transaction error
                print("")
                break
            else:
                print("******Account not closed because money is still in it******")#display invalid transaction error
                print("")
        else:
            print("******Invalid input try again******")
            print("")
fo.write("999999")
fo.close()
