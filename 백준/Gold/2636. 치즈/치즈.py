from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def melt():
    visited=[[0]*m for _ in range(n)]
    global arr
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    count=0
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0:
                if arr[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                elif arr[nx][ny]==1:
                    visited[nx][ny]=1
                    arr[nx][ny]=0
                    count+=1
    return count



n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]


result=0
turn=0
while True:
    cur_count=melt()
    if cur_count==0:
        break
    turn+=1
    result=cur_count
print(turn)
print(result)