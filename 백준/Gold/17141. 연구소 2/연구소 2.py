n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

pos_lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            pos_lst.append((i,j))

l=len(pos_lst)
dfs_visited=[0]*l
cur_lst=[]
result=1e9
from  collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def get_result():
    visited=[[0]*n for _ in range(n)]
    q=deque()
    answer=0
    for i in cur_lst:
        x,y=pos_lst[i]
        q.append(pos_lst[i])
        visited[x][y]=1
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!=1:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1

    answer=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=1 and visited[i][j]==0:
                return 1e9
            answer=max(answer,visited[i][j])
    return answer

def dfs(k,count):
    global dfs_visited,cur_lst,result
    if count>k:
        return
    if k==l:
        if count==m:
            temp=get_result()
            if temp==3:
                print(cur_lst)
            result=min(result,get_result())


        return

    dfs(k+1,count)

    cur_lst.append(k)
    dfs_visited[k]=1
    dfs(k+1,count+1)
    dfs_visited[k]=0
    cur_lst.pop()

dfs(0,0)
if result==1e9:
    print(-1)
else:
    print(result-1)