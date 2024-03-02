f,s,g,u,d=map(int,input().split())

visited=[0]*(f+1)

from collections import deque
q=deque()
q.append(s)
visited[s]=1

ud_lst=[u,-d]
while q:
    x=q.popleft()
    for t in ud_lst:
        nx=x+t
        if 1<=nx<=f and visited[nx]==0:
            q.append(nx)
            visited[nx]=visited[x]+1

#print(visited)
if visited[g]==0:
    print("use the stairs")
else:
    print(visited[g]-1)