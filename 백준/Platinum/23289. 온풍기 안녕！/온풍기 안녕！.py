

r,c,k=map(int,input().split())
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c
temp_arr=[list(map(int,input().split())) for _ in range(r)]

check_pos_lst=[]
arr=[[0]*c for _ in range(r)]

fan_pos_lst=[]

cd_lst=[0,1,3,0,2]
for i in range(r):
    for j in range(c):
        if temp_arr[i][j]==0:
            continue
        if temp_arr[i][j]==5:
            check_pos_lst.append((i,j))
        else:
            d=cd_lst[temp_arr[i][j]]
            fan_pos_lst.append((i,j,d))




wall_arr=[[[0,0,0,0] for _ in range(c)] for _ in range(r)]
w=int(input())
for _ in range(w):
    x,y,t=map(int,input().split())
    x-=1
    y-=1
    wall_arr[x][y][t]=1
    nx=x+dx[t]
    ny=y+dy[t]
    wall_arr[nx][ny][t+2]=1


def print_arr(arr):
    for i in range(r):
        print(arr[i])
    print()

from collections import deque
def wind(a,b,d):
    global arr,dic,fan_arr
    q=deque()
    sx=a+dx[d]
    sy=b+dy[d]
    q.append((sx,sy))
    visited=[[0]*c for _ in range(r)]
    visited[sx][sy]=5
    while q:
        x,y=q.popleft()
        if visited[x][y]==1:
            break

        #1
        d_lst=[(d+3)%4,(d+1)%4]

        # d-1,d / d / d+1,d
        lst=[[(d+3)%4,d],[d],[(d+1)%4,d]]
        for lst2 in lst:
            cx,cy=x,y
            flag=True
            for cur_d in lst2:
                cx=cx+dx[cur_d]
                cy=cy+dy[cur_d]
                if in_range(cx,cy) and visited[cx][cy]==0 and wall_arr[cx][cy][(cur_d+2)%4]==0:
                    continue
                else:
                    flag=False
            if flag:
                visited[cx][cy]=visited[x][y]-1
                q.append((cx,cy))
    #     for i in range(2):
    #         d0=d_lst[i]
    #         #벽 없고 범위 안, 방문x
    #         nx0=x+dx[d0]
    #         ny0=y+dy[d0]
    #         if in_range(nx0,ny0) and visited[nx0][ny0]==0 and wall_arr[x][y][d0]==0:
    #             nx1=nx0+dx[d]
    #             ny1=ny0+dy[d]
    #             if in_range(nx1,ny1) and visited[nx1][ny1]==0 and wall_arr[nx0][ny0][d]==0:
    #                 q.append((nx1,ny1))
    #                 visited[nx1][ny1]=visited[x][y]-1
    #     #2
    #
    #     nx=x+dx[d]
    #     ny=y+dy[d]
    #     if in_range(nx,ny) and visited[nx][ny]==0 and wall_arr[x][y][d]==0:
    #         q.append((nx,ny))
    #         visited[nx][ny]=visited[x][y]-1
    #
    # dic[(a,b,d)]=visited

    for i in range(r):
        for j in range(c):
            if visited[i][j]!=0:
                fan_arr[i][j]+=visited[i][j]


def fun2():
    global arr

    add_arr=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for d in range(1,3):
                nx=i+dx[d]
                ny=j+dy[d]
                if not in_range(nx,ny):
                    continue
                if wall_arr[i][j][d]==1:
                    continue
                dif=arr[nx][ny]-arr[i][j]
                #nx가 더 큼
                if dif>0:
                    abs_dif=dif//4
                    add_arr[nx][ny]-=abs_dif
                    add_arr[i][j]+=abs_dif

                elif dif <0:
                    abs_dif=(-dif)//4
                    add_arr[nx][ny]+=abs_dif
                    add_arr[i][j]-=abs_dif
    for i in range(r):
        for j in range(c):
            arr[i][j]+=add_arr[i][j]





def end_check():
    for x,y in check_pos_lst:
        if arr[x][y]<k:
            return False
    return True
result=0
dic=dict()

fan_arr=[[0]*c for _ in range(r)]
for x, y, d in fan_pos_lst:
    wind(x, y, d)


def wind_all():
    for i in range(r):
        for j in range(c):
            arr[i][j]+=fan_arr[i][j]


while True:
    if result==101:
        break

    # 1.바람이 한 번 나옴
    wind_all()

    # 2. 온도 조절
    fun2()


    # 3. 바깥 감소
    for i in range(r):
        for j in range(c):
            if arr[i][j]>0 and ( i==0 or i==r-1 or j==0 or j==c-1):
                arr[i][j]-=1



    result+=1

    if end_check():
        break


print(result)