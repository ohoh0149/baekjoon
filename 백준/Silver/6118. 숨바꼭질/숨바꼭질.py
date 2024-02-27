n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

q=deque()
visited=[0]*(n+1)
q.append(1)
visited[1]=1
while q:
    x=q.popleft()
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx]=visited[x]+1
            q.append(nx)
mi=max(visited)
c=0
for temp in visited:
    if mi==temp:
        c+=1

print(visited.index(mi),mi-1,c)