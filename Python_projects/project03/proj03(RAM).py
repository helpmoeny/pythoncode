N_str = input("Input a large whole number: ")
while N_str.isdigit()==False or int(N_str)<1:
    print("Input must be a whole number. Try again")
    N_str = input("Input a large whole number: ")
    

while True:
    spl_str=input("Split: ")
    if spl_str.isdigit()==False:
        print("Input must be a whole number. Try again")
    elif int(spl_str)<=0:
        print("Input must be a whole number. Try again")
    elif (int(len(N_str))%int(spl_str) != 0):
        print(N_str, " Must be evenly divisible by ",spl_str)
        print("Try again")
    else:
        break
            
count=0
num_str=''
output_str=''
increasing = True
last=0
s=int(spl_str)

nr_groups=int(len(N_str)/s)+1

for i in range (1,nr_groups):
    num_str=N_str[count*s:(count+1)*s]
    output_str+=num_str
    if i+1<nr_groups:
        output_str+=", "
    if int(num_str)<=last:
        increasing = False
    last=int(num_str)
    count+=1
    
print(output_str)
if increasing == True:
    print("Sequence is increasing")
else:
    print("Sequence is NOT Increasing")
