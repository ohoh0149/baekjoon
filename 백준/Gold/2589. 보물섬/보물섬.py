from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(i,j):
    global visited
    max_val=0
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    while q:
        x,y=q.popleft()
        max_val=max(max_val,visited[x][y])
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]=="L":
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return max_val-1
def init_visited():
    global visited
    for i in range(n):
        for j in range(m):
            visited[i][j]=0

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(input())

visited=[[0]*m for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if arr[i][j]=="L":
            init_visited()
            result=max(result,bfs(i,j))
#
print(result)

