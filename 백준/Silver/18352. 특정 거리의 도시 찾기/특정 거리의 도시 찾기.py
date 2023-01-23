from collections import deque
import sys
input= sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
#print(graph)
visited=[-1]*(n+1)
q=deque()
dis=0
q.append((x,dis))
visited[x]=dis

while q:
    a=q.popleft()
    distance= a[1]
    for v in graph[a[0]]:
        if visited[v]==-1:
            q.append((v,distance+1))
            visited[v]=distance+1
#print(visited)
if k not in visited:
    print(-1)
else:    
    for i in range(1,n+1):
        if visited[i] == k :
            print(i)
   
        