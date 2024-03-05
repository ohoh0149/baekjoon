n=int(input())
lst=[]
for _ in range(n):
    t,p=map(int,input().split())
    lst.append((t,p))

dp=[0]*n
dp.extend([0]*52)

for i in range(n-1,-1,-1):
    t,p=lst[i]
    if i+t>n:
        p=0
    dp[i]=max(dp[i+1],dp[i+t]+p)
print(dp[0])