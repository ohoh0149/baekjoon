n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
visited=[[0]*m for _ in range(n)]

result_count=0
max_count=0
for i in range(n):
    for j in range(m):
        if visited[i][j] or arr[i][j]==0:
            continue
        result_count+=1

        visited[i][j]=1
        count=1
        q=deque()
        q.append((i,j))
        while q:
            x,y=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==1:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    count+=1
        max_count=max(max_count,count)

print(result_count)
print(max_count)
