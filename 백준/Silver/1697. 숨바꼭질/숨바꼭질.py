from collections import deque
n,k=map(int,input().split())
visited=[0]*100001

q=deque()
q.append(n)
visited[n]=1
result=0

while q:
    x=q.popleft()
    if x==k:
        result=visited[x]-1
        break
    temp_lst=[x+1,x-1,2*x]
    for a in temp_lst:
        if not(0<=a<=100000):
            continue
        if visited[a]==0:
            visited[a]=visited[x]+1
            q.append(a)
print(result)