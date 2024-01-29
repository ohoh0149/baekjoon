s=input()


l=len(s)

se=set()
for i in range(1,l+1):
    for j in range(0,l-i+1):
        temp=s[j:j+i]
        se.add(temp)
        #print(temp)

print(len(se))
