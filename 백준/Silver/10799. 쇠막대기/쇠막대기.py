inp=input()

lst=[]
l=len(inp)
idx=0
while idx<l:
    if inp[idx]=="(" and inp[idx+1]==")":
        lst.append(".")
        idx+=2
        continue
    lst.append(inp[idx])

    idx+=1

count=0
result=0
for idx, s in enumerate(lst):
    if s=="(":
        count+=1
        result+=1
    elif s==".":
        result+=count
    else:
        count-=1

print(result)
