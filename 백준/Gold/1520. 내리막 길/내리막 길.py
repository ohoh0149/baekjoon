n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m


dp=[[-1]*m for _ in range(n)]
dp[0][0]=1
def dfs(x,y):

    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and arr[nx][ny]>arr[x][y]:
            dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

dfs(n-1,m-1)
print(dp[n-1][m-1])




