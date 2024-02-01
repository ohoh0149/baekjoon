n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
#print(arr)

dp=[[0]*3 for _ in range(n)]

#print(dp)
for i in range(3):
    dp[0][i]=arr[0][i]
for i in range(1,n):
    for j in range(3):
        min_val=1e9
        for k in range(3):
            if k==j:
                continue
            min_val=min(min_val,dp[i-1][k])
        dp[i][j]=min_val+arr[i][j]


print(min(dp[n-1]))