n=int(input())
lst=list(map(int,input().split()))
lst.sort()
sm=0
result=0
for i in range(n):
    result+=(sm+lst[i])
    sm+=lst[i]
print(result)

