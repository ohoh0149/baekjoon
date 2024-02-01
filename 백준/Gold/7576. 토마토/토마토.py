from collections import deque
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dx=[-1,0,1,0]
dy=[0,1,0,-1]

m,n=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]


pos_lst=[]
visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            pos_lst.append((i,j))
            visited[i][j]=1
q=deque(pos_lst)
while q:
    x,y=q.popleft()
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==0:
            q.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1


result=-1
fail_flag=False
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and visited[i][j]==0:
            fail_flag=True
            result=-1
            break
        result=max(result,visited[i][j]-1)

    if fail_flag:
        break

print(result)

