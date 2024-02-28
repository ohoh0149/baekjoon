n=int(input())

graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

visited=[0]*(n+1)
q=deque()
q.append(1)
visited[1]=1
while q:
    x=q.popleft()
    for nx in graph[x]:
        if not visited[nx]:
            q.append(nx)
            visited[nx]=x

for i in range(2,n+1):
    print(visited[i])