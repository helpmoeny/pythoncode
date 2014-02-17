import math
debt = input("What is the debt number:")
debt_float = float(debt)

dem_money = input("What denomination of currency:")
dem_money_float = float(dem_money)

height = (debt_float*.0043)/63360 #height of currency in miles

avg_moon = height/(238857)
debt_dem = height/dem_money_float

print()
print("The debt",debt,"has a height in miles of ",dem_money,"'s, ",debt_dem)
print("That is ",avg_moon," times the average distance from the earth to the moon")
