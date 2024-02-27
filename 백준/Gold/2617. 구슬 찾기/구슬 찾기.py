n,m=map(int,input().split())
graph1=[[] for _ in range(n)]
graph2=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph1[a].append(b)
    graph2[b].append(a)

result_visited=[0]*n
result=0
from collections import deque
for i in range(n):
    if graph1[i]:
        q=deque()
        q.append(i)
        count=0
        visited=[0]*n
        visited[i]=1
        while q:
            x=q.popleft()
            for nx in graph1[x]:
                if not visited[nx]:
                    q.append(nx)
                    visited[nx]=1
                    count+=1
        if count>n//2:
            result_visited[i]=1
            result+=1


for i in range(n):
    if result_visited[i]==1:
        continue
    if graph2[i]:
        q=deque()
        q.append(i)
        count=0
        visited=[0]*n
        visited[i]=1
        while q:
            x=q.popleft()
            for nx in graph2[x]:
                if not visited[nx]:
                    q.append(nx)
                    visited[nx]=1
                    count+=1
        if count>n//2:
            result_visited[i]=1
            result+=1

print(result)


