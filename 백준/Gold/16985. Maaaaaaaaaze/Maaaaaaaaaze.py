def rotate(arr):
    new_arr=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_arr[j][5-i-1]=arr[i][j]
    return new_arr


arr3=[]
for _ in range(5):
    arr2=[]
    for _ in range(5):
        arr2.append(list(map(int,input().split())))
    arr3.append(arr2)


dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,-1,1]
def in_range(x,y,z):
    return 0<=x<5 and 0<=y<5 and 0<=z<5
from collections import deque
def get_result(arr3):
    visited=[[[0]*5 for _ in range(5)] for _ in range(5)]
    q=deque()
    q.append((0,0,0))
    visited[0][0][0]=1
    while q:
        x,y,z=q.popleft()
        for d in range(6):
            nx=x+dx[d]
            ny=y+dy[d]
            nz=z+dz[d]
            if in_range(nx,ny,nz) and visited[nx][ny][nz]==0 and arr3[nx][ny][nz]==1:
                q.append((nx,ny,nz))
                visited[nx][ny][nz]=visited[x][y][z]+1

    if visited[4][4][4]!=0:
        return visited[4][4][4]-1
    else:
        return 1e9
result=1e9


dfs_visited=[0]*5
dfs_lst=[0]*5
def dfs(k):
    global result
    if result==12:
        return
    if k==5:
        new_arr3=[0]*5
        for i,temp in enumerate(dfs_lst):
            new_arr3[i]=arr3[temp]
        if new_arr3[0][0][0] != 1:
            return
        result=min(result,get_result(new_arr3))
        return
    for i in range(5):
        if dfs_visited[i]==0:
            dfs_visited[i]=1
            dfs_lst[k]=i
            dfs(k+1)
            dfs_lst[k]=0
            dfs_visited[i]=0




for _ in range(4):
    arr3[0]=rotate(arr3[0])
    for _ in range(4):
        arr3[1]=rotate(arr3[1])
        for _ in range(4):
            arr3[2] = rotate(arr3[2])
            for _ in range(4):
                arr3[3] = rotate(arr3[3])
                for _ in range(4):
                    arr3[4] = rotate(arr3[4])

                    # for i in range(5):
                    #     print(arr3[i])
                    #
                    dfs(0)

if result!=1e9:
    print(result)
else:
    print(-1)
    
    