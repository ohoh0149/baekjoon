s=input()

if len(s)==1:
    print(0)
    exit()

rev=[1,0]
result=0
if s[0]==s[-1]:
    r=str(1-int(s[0]))
    for i in range(1,len(s)):
        if s[i]==r and s[i-1]==s[0]:
            result+=1
else:
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            result+=1
    result+=1
    result//=2
print(result)
