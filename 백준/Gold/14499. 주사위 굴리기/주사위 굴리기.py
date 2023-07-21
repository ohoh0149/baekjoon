
def move(d):
    global dice
    #동 서 북 남

            # 2 4 1 3 5 6
    if d==1:
        dice=[dice[0],dice[5],dice[1],dice[2],dice[4],dice[3]]
    elif d==2:
        dice=[dice[0],dice[2],dice[3],dice[5],dice[4],dice[1]]
    elif d==3:
        dice=[dice[2],dice[1],dice[4],dice[3],dice[5],dice[0]]
    elif d==4:
        dice=[dice[5],dice[1],dice[0],dice[3],dice[2],dice[4]]




dice=[0,0,0,0,0,0]

n,m,x,y,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

d_list=list(map(int,input().split()))

dx=[-1,0,0,-1,1]
dy=[-1,1,-1,0,0]

def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
for d in d_list:
    nx=x+dx[d]
    ny=y+dy[d]
    if not in_range(nx,ny):
        continue
    else:
        x=nx
        y=ny
    move(d)
    if arr[x][y]==0:
        arr[x][y]=dice[5]
    else:
        dice[5]=arr[x][y]
        arr[x][y]=0
    print(dice[2])


