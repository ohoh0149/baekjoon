s=input()


k=0
p=0

if s[0]=="K":
    k+=1
else:
    p+=1

result=1
for t in s[1:]:
    if t=="K":
        k+=1
        if p>0:
            p-=1
    else:
        p+=1
        if k>0:
            k-=1
    result=max(result,k,p)

print(result)

