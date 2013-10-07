number_str = input("Enter a floating-point number: ")

while True:
    try:
        number_float = float(number_str)
        break
    except ValueError:
        print("This is not a floating-point number, try again")
        number_str = input("Enter a floating-point number: ")
print("Number is",number_float)
