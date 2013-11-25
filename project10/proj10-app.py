import Currency

print("A bank account named 'account' has $1000, you may enter a deduction amount")
print("(In the format 'XXX YYY', where xxx is the amount and yyy is the currencycode)")
print("or type 'q' to quit")
account=Currency.Currency(1000,'USD')
while True:
    fo=input("expense amount: ")
    if fo=="q" or fo=="Q":
        print("Quitting...")
        break
    else:
        try:
            line_str=fo.split(" ")
            amount=float(line_str[0])
            currencycode=line_str[1]

            expense=Currency.Currency(amount,currencycode)
            
            account=account-expense
        except:
            print("Incorrect inputs, try again...")
        
        zero=Currency.Currency(0,'USD')
        if zero>account:
            print("Overdrew account, quitting...")
            break
    print("Account now contains: ")
    print(account)
    print("")
