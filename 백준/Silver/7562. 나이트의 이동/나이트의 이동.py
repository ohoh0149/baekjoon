from  collections import deque
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
t=int(input())
for _ in range(t):
    l=int(input())
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())

    def in_range(x,y):
        return 0<=x<l and 0<=y<l

    visited=[[0]*l for _ in range(l)]

    visited[sx][sy]=1
    q=deque()
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            result=visited[x][y]-1
            break
        for d in range(8):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    print(result)