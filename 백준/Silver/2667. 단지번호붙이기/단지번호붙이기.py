from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(input()))

visited=[[0]*n for _ in range(n)]

lst=[]
count=0
for i in range(n):
    for j in range(n):
        if arr[i][j]=='0' or visited[i][j]!=0:
            continue
        count+=1
        q=deque()
        q.append((i,j))
        visited[i][j]=count
        temp=1
        while q:
            x,y=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]=='1':
                    q.append((nx,ny))
                    visited[nx][ny]=count
                    temp+=1
        lst.append(temp)

print(len(lst))
lst.sort()
for a in lst:
    print(a)