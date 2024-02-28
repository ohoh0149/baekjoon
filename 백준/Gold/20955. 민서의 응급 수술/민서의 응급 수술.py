import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0]*(n+1)
from collections import deque
group_count=0
result=0
for i in range(1,n+1):
    if visited[i]:
        continue
    group_count+=1

    edge_count=0
    node_count=1
    q=deque()
    q.append(i)
    visited[i]=1
    while q:
        x=q.popleft()
        for nx in graph[x]:
            edge_count+=1
            if visited[nx]==0:
                node_count+=1
                q.append(nx)
                visited[nx]=1
    edge_count//=2
    if edge_count>=node_count:
        result+=(edge_count-node_count+1)

result+=(group_count-1)

print(result)
