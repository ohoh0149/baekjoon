n=int(input())

dp=[-1]*(n+1)
dp[1]=0

for i in range(2,n+1):
    if i%3!=0:
        a=1e9
    else:
        a=dp[i//3]

    if i%2!=0:
        b=1e9
    else:
        b=dp[i//2]
    c=dp[i-1]

    dp[i]=min(a,b,c)+1
    #print(a,b,c)
    #print(i,dp[i])
print(dp[n])