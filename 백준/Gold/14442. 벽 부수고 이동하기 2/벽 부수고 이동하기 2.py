from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

n,m,k=map(int,input().split())
#arr=[list(map(int,input().split())) for _ in range(n)]
arr=[]
for _ in range(n):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(int(s))
    arr.append(lst)


visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]
#print(arr)
#print(visited)
q=deque()
q.append((0,0,0))
visited[0][0][0]=1
while q:
    x,y,c=q.popleft()
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        #print(nx,ny)
        if in_range(nx,ny):
            if arr[nx][ny]==0 and visited[nx][ny][c]==0:
                q.append((nx,ny,c))
                visited[nx][ny][c]=visited[x][y][c]+1
            elif arr[nx][ny]==1 and c<k and  visited[nx][ny][c+1]==0 :
                q.append((nx,ny,c+1))
                visited[nx][ny][c+1]=visited[x][y][c]+1

#print(visited)
result=1e9
for a in visited[n-1][m-1]:
    if a==0:
        continue
    result=min(result,a)

if result==1e9:
    result=-1
print(result)

