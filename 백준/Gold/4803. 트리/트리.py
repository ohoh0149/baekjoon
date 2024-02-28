from collections import deque

T=0
while True:
    T+=1

    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(n+1)
    tree_count=0
    for i in range(1,n+1):
        if visited[i]:
            continue
        isTree=True
        visited[i]=1
        q=deque()
        q.append(i)
        while q:
            x=q.popleft()
            for nx in graph[x]:
                if visited[nx]!=0 and visited[nx]!=visited[x]-1:
                    isTree=False
                    break
                if visited[nx]==0:
                    q.append(nx)
                    visited[nx]=visited[x]+1
        if isTree:
            tree_count+=1
    if tree_count==1:
        print("Case",str(T)+": There is one tree.")
    elif tree_count==0:
        print("Case",str(T)+": No trees.")
    else:
        print("Case",str(T)+": A forest of",tree_count,"trees.")

