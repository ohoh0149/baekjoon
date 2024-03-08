arr=[]
for _ in range(5):
    arr.append(input())


def get_next_pos(x,y):
    if y==4:
        return x+1,0
    else:
        return x,y+1


pos_lst=[]
visited=[[0]*5 for _ in range(5)]
from  collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=0
def in_range(x,y):
    return 0<=x<5 and 0<=y<5
def check():
    count=0
    for x,y in pos_lst:
        if arr[x][y]=="S":
            count+=1
    if count<4:
        return False

    q=deque()
    sx,sy=pos_lst[0]
    q.append(pos_lst[0])
    temp_visited=[[0]*5 for _ in range(5)]
    temp_visited[sx][sy]=1
    count=1
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==1 and temp_visited[nx][ny]==0:
                q.append((nx,ny))
                temp_visited[nx][ny]=1
                count+=1
    if count==7:
        return True
    else:
        return False
def dfs(x,y,count):
    global pos_lst,result
    if x==5 and y==0:
        if count==7:
            if check():
                result+=1
        return
    if count>7:
        return

    nx,ny=get_next_pos(x,y)
    dfs(nx,ny,count)

    pos_lst.append((x,y))
    visited[x][y]=1
    dfs(nx,ny,count+1)
    pos_lst.pop()
    visited[x][y]=0


dfs(0,0,0)
print(result)