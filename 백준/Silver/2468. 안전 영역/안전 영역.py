from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

max_count=0
for h in range(101):
    cur_count=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>h and visited[i][j]==0:
                cur_count+=1
                q=deque()
                q.append((i,j))
                visited[i][j]=1
                while q:
                    x,y=q.popleft()
                    for d in range(4):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]>h:
                            q.append((nx,ny))
                            visited[nx][ny]=1
    max_count=max(max_count,cur_count)
    if cur_count==0:
        break

print(max_count)