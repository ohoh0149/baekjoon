from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def get_d(a):
    lst=[0,1,3,2,0]
    return lst[a]

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
sx,sy,sd=map(int,input().split())
sd=get_d(sd)
ex,ey,ed=map(int,input().split())
ed=get_d(ed)
sx-=1
sy-=1
ex-=1
ey-=1

visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j]=[0,0,0,0]
result=0
q=deque()
q.append((sx,sy,sd))
visited[sx][sy][sd]=1
while q:
    x,y,d=q.popleft()
    if x==ex and y==ey and d==ed:
        result=visited[x][y][d]-1
    rd=(d+1)%4
    ld=(d-1+4)%4
    d_lst=[rd,ld]
    for cur_d in d_lst:
        if visited[x][y][cur_d]==0:
            q.append((x,y,cur_d))
            visited[x][y][cur_d]=visited[x][y][d]+1
    nx,ny=x,y
    for _ in range(3):
        nx=nx+dx[d]
        ny=ny+dy[d]
        if (not in_range(nx,ny)) or arr[nx][ny]==1:
            break
        if visited[nx][ny][d]==0:
            q.append((nx,ny,d))
            visited[nx][ny][d]=visited[x][y][d]+1



print(result)
























