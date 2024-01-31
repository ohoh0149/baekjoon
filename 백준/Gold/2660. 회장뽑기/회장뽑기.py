from collections import deque

n=int(input())
arr=[[0]*n for _ in range(n)]
while True:
    a,b=map(int,input().split())
    if a==-1:
        break
    arr[a-1][b-1]=1
    arr[b-1][a-1]=1

lst=[0]*n
for num in range(n):
    visited=[-1]*n
    q=deque()
    q.append(num)
    visited[num]=0
    while q:
        x=q.popleft()
        for i in range(n):
            if arr[x][i]==1 and visited[i]==-1:
                q.append(i)
                visited[i]=visited[x]+1
    lst[num]=max(visited)

min_num=min(lst)
a=lst.count(min_num)
print(min_num,a)
for i in range(n):
    if lst[i]==min_num:
        print(i+1,end=" ")



