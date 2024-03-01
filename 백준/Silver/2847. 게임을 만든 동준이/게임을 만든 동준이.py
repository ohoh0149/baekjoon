n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))


max_val=1e9
result=0
for i in range(n-1,-1,-1):
    if max_val>lst[i]:
        max_val=lst[i]
        continue
    else:
        result+=(lst[i]-max_val+1)
        max_val=max_val-1

print(result)