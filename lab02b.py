A,B,C = 0,0,0
for i in range(11):
    if i!=0 and i%2 == 0 and i%3 == 0:
        A += 1
        B += 1
    elif i%2 == 0:
        A += 1
    elif i%3 == 0:
        B += 1
    else:
        C += 1

print("A =", A)
print("B =", B)
print("C =", C)
print("i =", i)
