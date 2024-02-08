n=int(input())
a,b=map(int,input().split())
m=int(input())
arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    arr[x][y]=1
    arr[y][x]=1


from collections import deque

q=deque()
visited=[0]*(n+1)
q.append(a)
visited[a]=1
while q:
    x=q.popleft()
    if x==b:
        break
    for i in range(1,n+1):
        if visited[i]==0 and arr[x][i]==1:
            q.append(i)
            visited[i]=visited[x]+1

if visited[b]==0:
    print(-1)
else:
    print(visited[b]-1)
