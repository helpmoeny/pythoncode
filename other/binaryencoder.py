temp=input("Enter text: ")
newbinvalue=""
for ch in temp:
    newbinvalue+=bin(ord(ch))[2:]
print(newbinvalue)
