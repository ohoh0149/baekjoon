n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]=="R":
            rx,ry=i,j
            arr[i][j]="."
        elif arr[i][j]=="B":
            bx,by=i,j
            arr[i][j]="."
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#0이면 빨강 1이면 파랑
def who_first(rx,ry,bx,by,d):
    if d==0:
        if rx<bx:
            return 0
    elif d==1:
        if ry>by:
            return 0
    elif d==2:
        if rx>bx:
            return 0
    else:
        if ry<by:
            return 0
    return 1

#x,y에서 di방향으로 이동시켰을때의 위치 통과하면 -1,-1반환
def find_pos(x,y,x2,y2,di):
    while True:
        nx=x+dx[di]
        ny=y+dy[di]
        if nx==x2 and ny==y2:
            return x,y
        if arr[nx][ny]=="#":
            return x,y
        if arr[nx][ny]=="O":
            return -1,-1
        x,y=nx,ny




def move(rx,ry,bx,by,di):
    flag=who_first(rx,ry,bx,by,di)
    #빨강 먼저 이동
    if flag==0:
        rx,ry=find_pos(rx,ry,-1,-1,di)
        bx,by=find_pos(bx,by,rx,ry,di)
    else:
        bx,by=find_pos(bx,by,-1,-1,di)
        rx,ry=find_pos(rx,ry,bx,by,di)

    return rx,ry,bx,by

result=1e9
def dfs(k,rx,ry,bx,by,bdi):
    global result
    if result<=k:
        return
    if bx==-1:
        return
    if rx==-1:
        result=min(result,k)
        return
    if k==10:
        return

    for d in range(4):
        if d==bdi:
            continue
        nrx,nry,nbx,nby=move(rx,ry,bx,by,d)
        dfs(k+1,nrx,nry,nbx,nby,d)

dfs(0,rx,ry,bx,by,-1)
if result==1e9:
    print(-1)
else:
    print(result)

