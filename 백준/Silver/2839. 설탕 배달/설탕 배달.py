n=int(input())

if n<5:
    dp=[0]*10
else:
    dp=[-1]*(n+1)
dp[0]=0

dp[1]=-1
dp[2]=-1
dp[4]=-1
dp[3]=1
dp[5]=1
for i in range(6,n+1):
    a=dp[i-5]
    b=dp[i-3]
    if a==-1 and b==-1:
        dp[i]=-1
        continue
    if a==-1:
        a=1e9
    if b==-1:
        b=1e9
    dp[i]=min(a,b)+1
print(dp[n])


