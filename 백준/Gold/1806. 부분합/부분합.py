n,s=map(int,input().split())
lst=list(map(int,input().split()))

if lst[0]>=s:
    print(1)
    exit()
p1=0
p2=1
sm=lst[0]+lst[1]
result=1e9
while p2<n:
    if sm>=s:
        result=min(result,p2-p1+1)
        sm-=lst[p1]
        p1+=1
    else:
        p2+=1
        if p2==n:
            break
        sm+=lst[p2]

if result==1e9:
    print(0)
else:
    print(result)


