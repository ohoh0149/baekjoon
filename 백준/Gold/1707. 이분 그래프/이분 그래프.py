from collections import deque
k=int(input())
for _ in range(k):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(v+1)
    flag=True
    for num in range(1,v+1):
        if not flag:
            break
        if visited[num]!=0:
            continue
        q=deque()
        visited[num]=1
        q.append(num)
        while q:
            x=q.popleft()
            for nx in graph[x]:
                if visited[nx]==visited[x]:
                    flag=False
                    break
                if visited[nx]==0:
                    q.append(nx)
                    visited[nx]=-visited[x]

    if flag:
        print("YES")
    else:
        print("NO")

