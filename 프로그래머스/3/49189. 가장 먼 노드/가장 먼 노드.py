from collections import deque

def solution(n, edge):
    answer = 0
    visited=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q=deque()
    visited[1]=1
    q.append(1)
    while q:
        x=q.popleft()
        for nx in graph[x]:
            if visited[nx]!=0:
                continue
            visited[nx]=visited[x]+1
            q.append(nx)

    return visited.count(max(visited))
