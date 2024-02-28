n=int(input())
lst=list(map(int,input().split()))
rn=int(input())

route=-1
graph=[[] for _ in range(n)]
for c in range(n):
    p=lst[c]
    if p==-1:
        route=c
        continue
    graph[p].append(c)

from collections import deque
q=deque()
q.append(route)
visited=[0]*n
visited[route]=1
result=0
if route==rn:
    print(0)
    exit()
while q:
    x=q.popleft()
    count=0
    for nx in graph[x]:
        if nx!=rn:
            q.append(nx)
            count+=1
    if count==0:
        result+=1
print(result)

