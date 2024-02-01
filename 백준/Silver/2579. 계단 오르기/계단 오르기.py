n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

if n==1:
    print(lst[0])
    exit()
dp=[[0]*2 for _ in range(n)]
dp[0][0]=lst[0]
dp[0][1]=0
dp[1][0]=lst[1]
dp[1][1]=dp[0][0]+lst[1]

for i in range(2,n):
    dp[i][0]=max(dp[i-2])+lst[i]
    dp[i][1]=dp[i-1][0]+lst[i]
print(max(dp[n-1]))