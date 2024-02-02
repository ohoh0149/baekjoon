from collections import deque

m,n,h=map(int,input().split())
arr=[]
def in_range(x,y,z):
    return 0<=x<h and 0<=y<n and 0<=z<m
dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]
for _ in range(h):
    temp=[]
    for _ in range(n):
        temp.append(list(map(int,input().split())))
    arr.append(temp)

q=deque()
visited=[[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==1:
                q.append((i,j,k))
                visited[i][j][k]=1

while q:
    x,y,z=q.popleft()
    for d in range(6):
        nx=x+dx[d]
        ny=y+dy[d]
        nz=z+dz[d]
        if in_range(nx,ny,nz) and visited[nx][ny][nz]==0 and arr[nx][ny][nz]==0:
            q.append((nx,ny,nz))
            visited[nx][ny][nz]=visited[x][y][z]+1

zero_flag=False
max_val=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k]==0 and arr[i][j][k]!=-1:
                zero_flag=True
                break
            max_val=max(max_val,visited[i][j][k])

if zero_flag:
    print(-1)
else:
    print(max_val-1)