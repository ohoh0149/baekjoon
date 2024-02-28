n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,l=map(int,input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])

from collections import deque
def get_length(v1,v2):
    q=deque()
    visited=[-1]*(n+1)
    q.append(v1)
    visited[v1]=0
    while q:
        x=q.popleft()
        if x==v2:
            return visited[x]
        for nx,le in graph[x]:
            if visited[nx]==-1:
                q.append(nx)
                visited[nx]=visited[x]+le

for _ in range(m):
    a,b=map(int,input().split())
    print(get_length(a,b))