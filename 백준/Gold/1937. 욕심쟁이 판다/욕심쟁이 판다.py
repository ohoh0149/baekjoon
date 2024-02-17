n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

import sys
sys.setrecursionlimit(10**5)
dp=[[0]*n for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y):
    #print(x,y)
    if dp[x][y]!=0:
        return dp[x][y]
    flag=False
    for d in range(4):

        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and arr[nx][ny]<arr[x][y]:
            flag=True
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1)
    if not flag:
        dp[x][y]=1

    return dp[x][y]


#dfs(0,0)
for i in range(n):
    for j in range(n):
        #print("i,j",i,j)
        dfs(i,j)

result=0
for i in range(n):
    result=max(result,max(dp[i]))
print(result)