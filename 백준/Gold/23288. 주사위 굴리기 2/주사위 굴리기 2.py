from collections import  deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m


n,m,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

def change_d(a,b):
    global d
    if a>b:
        d=(d+1)%4
    elif a<b:
        d=(d+3)%4

def move_dice(d):
    global dice
    if d==0:
        dice=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif d==1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif d==2:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif d==3:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]


def get_point(x,y):
    q=deque()
    visited=[[0]*m for _ in range(n)]
    q.append((x,y))
    visited[x][y]=1
    num=arr[x][y]
    count=1
    while q:
        x,y=q.popleft()
        for di in range(4):
            nx=x+dx[di]
            ny=y+dy[di]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==num:
                count+=1
                q.append((nx,ny))
                visited[nx][ny]=1
    return count*num


dx=[-1,0,1,0]
dy=[0,1,0,-1]

dice=[1,2,3,4,5,6]
x,y=0,0
d=1
result=0
for _ in range(k):
    nx=x+dx[d]
    ny=y+dy[d]
    if not in_range(nx,ny):
        d=(d+2)%4
        nx=x+dx[d]
        ny=y+dy[d]
    x,y=nx,ny
    move_dice(d)
    result+=get_point(x,y)
    change_d(dice[5],arr[x][y])
print(result)



