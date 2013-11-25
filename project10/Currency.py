import urllib.request

class Currency( object ):
    def __init__(self,amount=0,currencycode=""):
        """Initialize an object of type Currency"""
        self.__amount = 0
        self.__currencycode = ""

        print(amount)
        print(currencycode)
        if isinstance(amount,int) or isinstance(amount,float) and isinstance(currencycode,str):
            self.__amount=amount
            self.__currencycode=currencycode
        else:
            print('error input type')
            amount = self.__amount
            currencycode = self.__currencycode
            
    def __repr__( self ):
        """
        Return a string (the representation of a Currency).
        """
        amount=self.__amount
        currencycode=self.__currencycode
        return("{:.2f}, {}".format(amount,currencycode))

    def __str__( self ):
        """
        Return a string (the representation of a Currency).
        """
        #same as __repr__
        amount=self.__amount
        currencycode=self.__currencycode
        return("Amount= {:.2f}, Currency: {}".format(amount,currencycode))
    
    def convert_to(self,newcurrencycode):
        amount=self.__amount
        currencycode=self.__currencycode
        if newcurrencycode=='USD' or newcurrencycode=='EUR' or newcurrencycode=='SEK' or newcurrencycode=='CAD' or newcurrencycode=='CNY' or newcurrencycode=='GDP':
            web_obj = urllib.request.urlopen("https://www.google.com/finance/converter?a="+str(amount)+"&from="+currencycode+"&to="+newcurrencycode+"")
            results_str = str(web_obj.read())
            web_obj.close()

            line_lst=results_str.split('currency_converter_result')
            currency_str= ''.join(c for c in line_lst[1] if c not in '(){}<>&abcdefghijklmnopqrstuvwxyz/\=#;:"')

            #print(x) #whole document, after split(list)
            #print(x[1]) #line i want from list
            #print(currency_str) #broken down line

            currency_lst=currency_str.split(" ") #0,1  4,5
            #print(currency_lst) #broken down list of broken down line

            new_amount=float(currency_lst[4])
            new_currency=currency_lst[5]

            old_amount=currency_lst[0]
            old_currency=currency_lst[1]

        else:
            print("Incorrect Currency type")
        return Currency(new_amount,new_currency)

    def __add__(self, other):
        if isinstance(other,Currency):
            #add the two currencies
            other_currency = other.convert_to(self.__currencycode)
            self.__amount=self.__amount+other.amount#wrong
        if isinstance(other,int) or isinstance(other,float):
            new_amount=self.__amount+other
            return Currency(new_amount,self.__currencycode)

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        if isinstance(other,Currency):
            #subtract the two currencies
        if isinstance(other,int) or isinstance(other,float):
            new_amount=self.__amount-other
            return Currency(new_amount,self.__currencycode)

    def __rsub__(self, other):
        pass

    

usa=Currency(10,'USD')
germany=usa.convert_to('EUR')
