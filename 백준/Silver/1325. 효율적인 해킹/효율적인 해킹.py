n,m=map(int,input().split())
import sys
input=sys.stdin.readline
arr=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[b].append(a)


from collections import deque
lst=[0]*(n+1)
for i in range(1,n+1):
    count=1
    q=deque()
    q.append(i)
    visited=[0]*(n+1)
    visited[i]=1
    while q:
        x=q.popleft()
        for nx in arr[x]:
            if visited[nx]==0:
                count+=1
                visited[nx]=1
                q.append(nx)
    lst[i]=count
#print(lst)
m=max(lst)
for i in range(1,n+1):
    if lst[i]==m:
        print(i,end=" ")


