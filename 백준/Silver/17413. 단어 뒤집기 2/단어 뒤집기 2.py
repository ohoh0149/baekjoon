s=input()

result=""
stack=[]

temp=""
mode=0
for c in s:
    if mode==1:
        temp+=c
        if c==">":
            mode=0
            result+=temp
            temp=""
        continue

    if c=="<":
        if temp:
            result+=temp
        mode=1
        temp="<"
    elif c==" ":
        temp+=c
        result+=temp
        temp=""

    else:
        temp=c+temp

result+=temp

print(result)






