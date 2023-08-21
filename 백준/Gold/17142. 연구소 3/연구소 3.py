from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

def get_result():
    q=deque()
    visited=[[0]*n for _ in range(n)]
    for vx,vy in choose_virus_lst:
        q.append((vx,vy))
        visited[vx][vy]=1

    find_blank_count=0
    res=-1
    while q:
        x,y=q.popleft()
        if arr[x][y]==0:
            find_blank_count+=1
        if find_blank_count==blank_count:
            res=visited[x][y]-1
            break
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!=1:
                # if arr[nx][ny]==0:
                #     find_blank_count+=1
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
    #print(visited)
    return res








def dfs(k,count):
    global result
    global choose_virus_lst
    if count>m:
        return
    if k==l:
        if count==m:
            temp_result=get_result()
            if temp_result!=-1:
                result=min(result,temp_result)
        return

    dfs(k+1,count)
    choose_virus_lst.append(total_virus_lst[k])
    dfs(k+1,count+1)
    choose_virus_lst.pop()


n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
total_virus_lst=[]

blank_count=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            total_virus_lst.append((i,j))
        elif arr[i][j]==0:
            blank_count+=1

result=1e9
l=len(total_virus_lst)
choose_virus_lst=[]
dfs(0,0)
if result==1e9:
    print(-1)
else:
    print(result)

