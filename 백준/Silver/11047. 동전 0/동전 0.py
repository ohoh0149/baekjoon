n,k=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

result=0
while lst:
    if k==0:
        break
    p=lst.pop()
    if p<=k:
        result+=(k//p)
        k=k%p

print(result)

