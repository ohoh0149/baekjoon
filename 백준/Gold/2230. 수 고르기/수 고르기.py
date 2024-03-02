n,m=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))
lst.sort()
idx1=0
idx2=0
max_val=1e11
while idx2<n and idx1<n:
    a,b=lst[idx1],lst[idx2]
    if b-a==0:
        if m==0:
            max_val=0
        idx2+=1
        continue
    if b-a<m:
        idx2+=1
        continue
    else:
        idx1+=1
        max_val=min(max_val,b-a)
print(max_val)