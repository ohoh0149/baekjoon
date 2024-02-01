from collections import deque

n=int(input())
m=int(input())
arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1

q=deque()
q.append(1)
visited=[0]*(n+1)
visited[1]=1
result=0
while q:
    x=q.popleft()
    for i in range(1,n+1):
        if arr[x][i]==1 and visited[i]==0:
            q.append(i)
            visited[i]=1
            result+=1
print(result)
