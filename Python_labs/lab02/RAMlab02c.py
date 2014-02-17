# Declare and initialize variables
even_count=0
odd_count=0
even_sum=0
odd_sum=0

# Main loop
while True:
    Int_input = input("Input an integer (Enter '0' to End Entry) --> ")
    Int = int(Int_input)
    # check for 0 and exit loop
    if Int == 0:
        print("Ending Input")
        break

    # Check for negative numbers and alert
    elif Int < 0: 
        print("No negative integers")

    # Find even numbers    
    elif Int % 2 == 0: 
        print("That's Even...")
        even_sum = even_sum+Int
        even_count = even_count+1

    # Treat as odd by default
    else:
        print("That's Odd...")
        odd_sum = odd_sum+Int
        odd_count = odd_count+1

# Display Results
print("")
print("Results:")
print("Sum of even numbers entered     :",even_sum,)
print("Sum of odd numbers entered      :",odd_sum)
print("Number of even integers entered :",even_count)
print("Number of odd integers entered  :",odd_count)
print("")
if even_sum > odd_sum:
    print("Evens Win")
else:
    print("Odds Win")

