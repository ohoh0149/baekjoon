n=int(input())
lst=[0]
for _ in range(n):
    lst.append(int(input()))

if n==1:
    print(lst[1])
    exit()
dp=[[0]*3 for _ in range(n+1)]


dp[1][0]=lst[1]
for i in range(2,n+1):
    dp[i][0]=lst[i]+max(dp[i-2])
    dp[i][1]=lst[i]+dp[i-1][0]
    dp[i][2]=max(dp[i-1])

print(max(max(dp[n]),max(dp[n-1])))

