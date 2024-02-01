from collections import deque
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dx=[-1,0,1,0]
dy=[0,1,0,-1]

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())

    arr=[[0]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        arr[b][a]=1

    # for i in range(n):
    #     print(arr[i])
    #
    result=0
    visited=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                continue
            if visited[i][j]==1:
                continue
            result+=1
            visited[i][j]=1
            q=deque()
            q.append((i, j))
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==1:
                        q.append((nx,ny))
                        visited[nx][ny]=1
    print(result)


