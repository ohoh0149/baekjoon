n,m,g,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

can_lst=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            can_lst.append((i,j))


l=len(can_lst)
red_lst=[]
green_lst=[]
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def get_result():
    visited=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            visited[i][j]=[0,0]
    q=deque()
    for x,y in red_lst:
        visited[x][y]=[1,1]
        q.append((x,y))
    for x,y in green_lst:
        visited[x][y]=[1,2]
        q.append((x,y))

    while q:
        x,y=q.popleft()
        if visited[x][y][1]==3:
            continue
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if not in_range(nx,ny):
                continue
            if arr[nx][ny]==0:
                continue
            if visited[nx][ny][1]==3:
                continue

            if visited[nx][ny][0] ==0 or (visited[nx][ny][0]==visited[x][y][0]+1 and visited[nx][ny][1]!=visited[x][y][1]):
                q.append((nx,ny))
                visited[nx][ny][0] = visited[x][y][0] + 1
                visited[nx][ny][1]+=visited[x][y][1]



    count=0
    for i in range(n):
        for j in range(m):
            if visited[i][j][1]==3:
                count+=1



    return count
result=0

def dfs(k,r_count,g_count):
    global result,red_lst,green_lst
    if r_count>r or g_count>g:
        return
    #남은 개수 l-k
    if l-k<r-r_count+g-g_count:
        return
    if k==l:
        if r_count==r and g_count==g:
            pass
            #print(red_lst,green_lst)
            #get_result()
            result=max(result,get_result())
        return

    dfs(k+1,r_count,g_count)
    red_lst.append((can_lst[k]))
    dfs(k+1,r_count+1,g_count)
    red_lst.pop()

    green_lst.append((can_lst[k]))
    dfs(k+1,r_count,g_count+1)
    green_lst.pop()




dfs(0,0,0)
print(result)