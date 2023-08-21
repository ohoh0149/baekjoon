from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def find_fish():
    move_count=1e9
    q=deque()
    visited=[[0]*n for _ in range(n)]
    q.append((sx,sy))
    visited[sx][sy]=1
    pos_lst=[]
    while q:
        x,y=q.popleft()
        if visited[x][y]>move_count:
            break
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]<=sw :
                if arr[nx][ny]==0 or arr[nx][ny]==sw:
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                elif arr[nx][ny]<sw:
                    pos_lst.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    if move_count==1e9:
                        move_count=visited[x][y]
    if len(pos_lst)==0:
        return -1,-1,-1
    else:
        pos_lst.sort()
        return pos_lst[0][0],pos_lst[0][1],move_count





n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

sx,sy,sw,eat_count=-1,-1,2,0
for i in range(n):
    for j in range(n):
        if arr[i][j]==9:
            sx,sy=i,j
            arr[i][j]=0
            break
    if sx!=-1:
        break

result=0
while True:
    nsx,nsy,mc=find_fish()
    if nsx==-1:
        break
    sx,sy=nsx,nsy
    result+=mc
    arr[sx][sy]=0
    eat_count+=1
    if sw==eat_count:
        sw+=1
        eat_count=0
print(result)


