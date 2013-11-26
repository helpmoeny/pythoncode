import currency
print("USA")
usa=currency.Currency(7.50,'USD')
print(usa)
print("")

print("Germany")
germany=currency.Currency(2,'EUR')
print(germany)
print("")

new_curr=germany.convert_to('USD')
print(new_curr)
print("")

sum_curr= usa+germany
print(sum_curr)
print("")

sum_curr2= usa+5.5
print(sum_curr2)
print("")

sum_curr3= 5+germany
print(sum_curr3)
print("")

sub_curr= usa-germany
print(sub_curr)
print("")

anothersub_curr= germany-usa
print(anothersub_curr)
print("")

rsub_curr= 9-usa
print(rsub_curr)
print("")

print("Is USA's currency amount greater than Germany?")
gt_curr= usa>germany
lt_curr= germany>usa
print(gt_curr)
print("Is Germany's currency amount greater than USA's?")
print(lt_curr)
print("")
