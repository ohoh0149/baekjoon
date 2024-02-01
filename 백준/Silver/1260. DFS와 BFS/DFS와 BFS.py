import sys
input=sys.stdin.readline
from collections import deque
n,m,v=map(int,input().split())

arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1

visited=[0]*(n+1)
visited[v]=1
def dfs(u):
    print(u,end=" ")
    for i in range(1,n+1):
        if arr[u][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(i)
dfs(v)

print()
q=deque()
q.append(v)
visited=[0]*(n+1)
visited[v]=1
while q:
    x=q.popleft()
    print(x,end=" ")
    for i in range(1,n+1):
        if arr[x][i]==1 and visited[i]==0:
            q.append(i)
            visited[i]=1
