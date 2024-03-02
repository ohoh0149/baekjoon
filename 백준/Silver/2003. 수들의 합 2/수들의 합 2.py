n,m=map(int,input().split())
lst=list(map(int,input().split()))

if n==1:
    if lst[0]==m:
        print(1)
    else:
        print(0)

    exit()

p1=0
p2=0
sm=lst[p1]
result=0
while p2<n:
    if sm<=m or p1==p2:
        if sm==m:
            result+=1
        p2+=1
        if p2==n:
            break
        sm+=lst[p2]
    else:
        sm-=lst[p1]
        p1+=1
print(result)
