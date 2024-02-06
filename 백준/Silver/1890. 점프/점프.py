n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dp=[[0]*n for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue

        for r in range(i):
            # r,j
            if dp[r][j]>0 and r+arr[r][j]==i:
                dp[i][j]+=dp[r][j]

        for c in range(j):
            # i,c
            if dp[i][c]>0 and c+arr[i][c]==j:
                dp[i][j]+=dp[i][c]
print(dp[n-1][n-1])
