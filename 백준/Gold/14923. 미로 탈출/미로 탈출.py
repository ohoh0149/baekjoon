from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
#
# def get_w_lst():
#     lst=[]
#
#     visited = [[0] * m for _ in range(n)]
#     q = deque()
#     q.append((hx, hy))
#     visited[hx][hy] = 1
#     while q:
#         x, y = q.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if in_range(nx, ny) and visited[nx][ny] == 0:
#                 if arr[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx, ny))
#                 if arr[nx][ny]==1:
#                     visited[nx][ny]=1
#                     lst.append((nx,ny))
#
#     return lst
def get_result():
    visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append((hx,hy,0))
    visited[hx][hy][0]=1
    while q:
        x,y,c=q.popleft()
        if x==ex and y==ey:
            # for i in range(n):
            #     print(visited[i])
            return visited[ex][ey][c]-1
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny][c]==0 and arr[nx][ny]==0:
                visited[nx][ny][c]=visited[x][y][c]+1
                q.append((nx,ny,c))
            if in_range(nx,ny) and visited[nx][ny][c]==0 and arr[nx][ny]==1 and c==0:
                visited[nx][ny][c+1]=visited[x][y][c]+1
                q.append((nx,ny,c+1))
    return -1


n,m=map(int,input().split())
hx,hy=map(int,input().split())
ex,ey=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
hx-=1
hy-=1
ex-=1
ey-=1

result=get_result()
print(result)

