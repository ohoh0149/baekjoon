from collections import  deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def melt():
    global total_ice_count
    global arr
    minus_arr=[[0]*m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j]>0:
                count=0
                for d in range(4):
                    nx=i+dx[d]
                    ny=j+dy[d]
                    if arr[nx][ny]==0:
                        count+=1
                minus_arr[i][j]=-count
    for i in range(1,n-1):
        for j in range(1,m-1):
            if minus_arr[i][j]>=0:
                continue
            arr[i][j]+=minus_arr[i][j]
            if arr[i][j]<=0:
                arr[i][j]=0
                total_ice_count-=1


def print_arr(arr):
    for i in range(1,n-1):
        for j in range(1,m-1):
            print(arr[i][j],end=" ")
        print()
    print()


def check_end():
    sx=-1
    sy=-1
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i][j]>0:
                sx,sy=i,j
                break
        if sx!=-1:
            break
    #종료한다
    if sx==-1:
        return True
    #sx,sy 에서 bfs
    #print(sx,sy)
    q=deque()
    q.append((sx,sy))
    visited=[[0]*m for _ in range(n)]
    visited[sx][sy]=1
    cur_ice_count=1
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if arr[nx][ny]>0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                cur_ice_count+=1
    if cur_ice_count!=total_ice_count:
        return True
    else:
        return False







n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

total_ice_count=0
for i in range(1,n-1):
    for j in range(1,m-1):
        if arr[i][j]>0:
            total_ice_count+=1

#print(total_ice_count)
result=0
while total_ice_count>0:
    result+=1
    melt()
    if total_ice_count==0:
        break
    #print_arr(arr)
    #print(total_ice_count)
    if check_end():
        break

if total_ice_count==0:
    print(0)
else:
    print(result)
