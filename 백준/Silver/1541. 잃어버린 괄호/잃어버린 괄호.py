inp=input()

lst=inp.split("-")

temp=[]
for s in lst:
    ls=s.split("+")
    temp.append(sum(list(map(int,ls))))

result=temp.pop(0)
for t in temp:
    result-=t
print(result)
