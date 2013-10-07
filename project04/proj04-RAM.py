from math import exp, expm1
import os
#define variables:
#another comment
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
                if deposit+balance > 9999999.99:#check input for errors
                    print("Can't Deposit that much...")
                else:
                    balance = balance + deposit
            except ValueError:
                print("Incorrect input, try again...")
        elif trans == "w":
            withdrawal_in=input("Withdrawal amount: ")#prompt for withdrawl amount
            try:
                withdrawl=float(withdrawal_in)
                if withdrawl > balance:#check input for errors
                    print("Can't withdraw that much...")
                else:
                    balance = balance - withdrawl
            except ValueError:
                print("Incorrect input, try again...")
        elif trans == "a":
            out_line=account_nr+" "+ str("{0:.2f}".format(balance)).rjust(10)+ " "+name
            fo.write(out_line)
            #do nothing just go to next record
            break
        elif trans == "c":
            if equal_floats(balance,0)==True:
                break
            else:
                print("Account not closed because money is still in it.")#display invalid transaction error
        else:
            print("Invalid input try again...")
fo.write("999999")
fo.close()
