from collections import deque


def in_range(x,y):
    return 0<=x<h and 0<=y<w

k=int(input())
w,h=map(int,input().split())
arr=[]
for _ in range(h):
    arr.append(list(map(int,input().split())))

dx=[-1,0,1,0,-2,-1,1,2,2,1,-1,-2]
dy=[0,1,0,-1,1,2,2,1,-1,-2,-2,-1]

visited=[[[0]*31 for _ in range(w)] for _ in range(h)]
# for i in range(h):
#     for j in range(w):
#         print(visited[i][j],end=" ")
#     print()
#print(visited)
k_count=0
q=deque()
q.append((0,0,0))
visited[0][0][0]=1

while q:
    x,y,count=q.popleft()
    for d in range(12):
        nx=x+dx[d]
        ny=y+dy[d]
        if not in_range(nx,ny) or arr[nx][ny]==1:
            continue
        if d<=3:
            if visited[nx][ny][count]==0:
                q.append((nx,ny,count))
                visited[nx][ny][count]=visited[x][y][count]+1
        else:
            if count<k:
                if visited[nx][ny][count+1]==0:
                    q.append((nx,ny,count+1))
                    visited[nx][ny][count+1]=visited[x][y][count]+1
#
# for i in range(h):
#     for j in range(w):
#         print(visited[i][j],end=" ")
#     print()

result=1e9
for i in range(31):
    if visited[h-1][w-1][i]!=0:
        result=min(result,visited[h-1][w-1][i]-1)
if result==1e9:
    print(-1)
else:
    print(result)













