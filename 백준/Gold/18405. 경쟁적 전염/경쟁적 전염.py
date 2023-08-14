from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
s,sx,sy=map(int,input().split())


virus_lst=[[] for _ in range(k+1)]

for i in range(n):
    for j in range(n):
        if arr[i][j]>0:
            virus_lst[arr[i][j]].append((i,j))
q=deque()
for viruses in virus_lst:
    for x,y in viruses:
        q.append((x,y,0))
while q:
    x,y,turn=q.popleft()
    if turn ==s:
        break
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and arr[nx][ny]==0:
            arr[nx][ny]=arr[x][y]
            q.append((nx,ny,turn+1))


print(arr[sx-1][sy-1])

