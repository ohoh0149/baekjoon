from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))
#print(graph)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
q.append((0,0))
visited=[[0]*m for i in range(n)]
visited[0][0]=1
while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and graph[nx][ny]=="1":
            q.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1
print(visited[n-1][m-1])

