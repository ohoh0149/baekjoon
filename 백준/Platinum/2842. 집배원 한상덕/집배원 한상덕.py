n=int(input())
arr=[list(input()) for _ in range(n)]
h_arr=[list(map(int,input().split())) for _ in range(n)]

k_count=0
h_lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]=="P":
            px,py=i,j
        if arr[i][j]=="K":
            k_count+=1
        h_lst.append(h_arr[i][j])
h_lst.sort()
h_set=set(h_lst)
h_lst=list(h_set)

le=len(h_lst)
l=0
r=0
from collections import  deque
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def check(low,high):

    if not low<=h_arr[px][py]<=high:
        return False
    q=deque()
    q.append((px,py))
    visited=[[0]*n for _ in range(n)]
    visited[px][py]=1
    count=0
    while q:
        x,y=q.popleft()
        for d in range(8):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and low<=h_arr[nx][ny]<=high:
                q.append((nx,ny))
                visited[nx][ny]=1
                if arr[nx][ny]=="K":
                    count+=1
    if count==k_count:
        return True



result=1000000
while l<le:
    flag=check(h_lst[l],h_lst[r])

    if not flag:
        if r+1<le:
            r+=1
        else:
            break
    else:
        result=min(result,h_lst[r]-h_lst[l])
        l+=1
print(result)




