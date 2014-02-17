str2="anteater"
str1="ants"
print(str1!=str2)
#string 1 does not equal string 2
print(str1>str2)
#comparing the individual characters of the string, the first string is greater then the second!
print(len(str1)<len(str2))
#the length of each string isn't the same, and the length of string 2 is longer then string 1

S="Spartans"
i = 0
while i < len(S):
    print (i,S[i])
    i += 1

#ALTERNATIVE
#text=list(S)
#while text:
    #print(text.pop())
    
i=0
for i in range(len(S)):
    print (i,S[i])
    i=i+1

for i, c in enumerate(S):
    print (i,c)
#for c in S:
    #print (c)
#This works as well!
