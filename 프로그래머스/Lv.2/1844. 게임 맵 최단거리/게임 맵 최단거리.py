from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
n=0
m=0
def solution(maps):
    global n,m
    answer = 0
    n=len(maps)
    m=len(maps[0])
    
    visited=[[0]*m for _ in range(n)]
    q=deque()
    visited[0][0]=1
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and maps[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    
    answer=visited[n-1][m-1]
    if answer==0:
        answer=-1
    return answer