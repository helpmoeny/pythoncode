Int_input = input("Input an integer (0 terminates) ")
Int = int(Int_input)
while Int !=0:
    Int_input = input("Input an integer (0 terminates) ")
    Int = int(Int_input)
    if Int % 2 ==0:
            print("even")
    else:
            print("odd")
