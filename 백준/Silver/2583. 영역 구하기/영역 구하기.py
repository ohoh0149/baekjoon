m,n,k=map(int,input().split())
arr=[[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1


from collections import deque
def in_range(x,y):
    return 0<=x<n and 0<=y<m
dx=[-1,0,1,0]
dy=[0,1,0,-1]
lst=[]
visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and visited[i][j]==0:
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            count=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==0:
                        q.append((nx,ny))
                        visited[nx][ny]=1
                        count+=1
            lst.append(count)
print(len(lst))
lst.sort()
print(*lst)



