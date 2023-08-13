
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

def get_length(x1,y1,x2,y2):
    visited=[[0]*m for _ in range(n)]
    q=deque()
    q.append((x1,y1))
    visited[x1][y1]=1
    while q:
        x,y=q.popleft()
        if x==x2 and y==y2:
            break
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!="#":
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return visited[x2][y2]-1


def get_total_length():
    x,y=sx,sy
    result=0
    for num in choose_num_lst:
        nx,ny=pos_lst[num]
        result+=get_length(x,y,nx,ny)
        if result>=ans:
            return result
        x,y=nx,ny
    result+=get_length(x,y,ex,ey)
    return result

visited_num=[0]*6
def dfs(k):
    global ans
    l=len(pos_lst)
    if k==l:
        ans=min(get_total_length(),ans)
        return
    for i in range(l):
        if visited_num[i]==0:
            visited_num[i]=1
            choose_num_lst.append(i)
            dfs(k+1)
            visited_num[i]=0
            choose_num_lst.pop()

m,n=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(input())
pos_lst=[]
sx,sy=-1,-1
ex,ey=-1,-1
for i in range(n):
    for j in range(m):
        if arr[i][j]=="X":
            pos_lst.append((i,j))
        elif arr[i][j]=="S":
            sx,sy=i,j
        elif arr[i][j]=="E":
            ex,ey=i,j

ans=1e9
choose_num_lst=[]
dfs(0)
print(ans)