import copy
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def make_outside():
    q=deque()
    visited=[[0]*m for _ in range(n)]
    q.append((0,0))
    visited[0][0]=1
    arr[0][0]=2
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==0:
                visited[nx][ny]=1
                arr[nx][ny]=2
                q.append((nx,ny))







n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

total_count=0
make_outside()
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            total_count+=1

def print_arr(arr):
    for i in range(n):
        print(arr[i])

def bfs(sx,sy):
    #print("bfs",sx,sy)
    global new_arr
    q=deque()
    q.append((sx,sy))
    new_arr[sx][sy]=2
    while q:
        x,y=q.popleft()
        #print(x,y)
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and arr[nx][ny]==0 and new_arr[nx][ny]!=2:
                new_arr[nx][ny]=2
                q.append((nx,ny))

turn=0
while total_count>0:
    turn+=1
    new_arr=copy.deepcopy(arr)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j]==1:
                count=0
                flag=0
                #외부와 접촉 얼마나 하고있는지 확인

                for d in range(4):
                    nx=i+dx[d]
                    ny=j+dy[d]
                    if arr[nx][ny]==2:
                        count+=1
                    if arr[nx][ny]==0:
                        flag=1
              #  print(i,j,count)
                if count>=2:
                    total_count-=1
                    if flag==0:
                        new_arr[i][j]=2
                    else:
                        bfs(i,j)
    arr=new_arr
    # print_arr(arr)
    # print(total_count)
    # print()

print(turn)