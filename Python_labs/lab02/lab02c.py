even_count=0
odd_count=0
even_sum=0
odd_sum=0
Int = 1
while Int !=0:
    Int_input = input("Input an integer (0 terminates) ")
    Int = int(Int_input)
    if Int % 2 ==0:
        if Int >0:
            print("even")
            even_sum=even_sum+Int
            even_count=even_count+1
        else:
            print("No negative integers")
    else:
            if Int >0:
                print("odd")
                odd_sum=odd_sum+Int
                odd_count=odd_count+1
            else:
                print("No negative integers")
    print("")
print("")
print("Sum of even numbers entered ",even_sum,"   Sum of odd numbers entered ",odd_sum)
print("even numbers entered ",even_count,"        odd numbers entered ",odd_count)


