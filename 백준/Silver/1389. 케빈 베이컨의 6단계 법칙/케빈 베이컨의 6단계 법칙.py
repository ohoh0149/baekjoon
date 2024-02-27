from collections import deque

n,m=map(int,input().split())
arr=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def get_count(num):
    visited=[-1]*(n+1)
    q=deque()
    visited[num]=0
    q.append(num)
    while q:
        x=q.popleft()
        for nx in arr[x]:
            if visited[nx]==-1 :
                visited[nx]=visited[x]+1
                q.append(nx)
    return sum(visited)

min_count=1e9
min_num=-1
lst=[]
for i in range(1,n+1):
    count=get_count(i)
    lst.append(count)
print(lst.index(min(lst))+1)

