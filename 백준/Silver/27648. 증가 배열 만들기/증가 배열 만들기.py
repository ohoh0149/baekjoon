from collections import deque

n,m,k=map(int,input().split())
visited=[[0]*m for _ in range(n)]
q=deque()
q.append((0,0))
dx=[1,0]
dy=[0,1]
visited[0][0]=1
def in_range(x,y):
    return 0<=x<n and 0<=y<m
while q:
    x,y=q.popleft()
    for d in range(2):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and visited[nx][ny]==0:
            q.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1

if visited[n-1][m-1]<=k:
    print("YES")
    for i in range(n):
        print(*visited[i])
else:
    print("NO")

