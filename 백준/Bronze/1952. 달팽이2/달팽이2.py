n,m=map(int,input().split())

arr=[[0]*m for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

x,y=0,0
d=0
result=0
def in_range(x,y):
    return 0<=x<n and 0<=y<m
for i in range(1,n*m+1):
    arr[x][y]=i
    nx=x+dx[d]
    ny=y+dy[d]
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        result+=1
        d=(d+1)%4
        nx=x+dx[d]
        ny=y+dy[d]
    x,y=nx,ny

print(result-1)