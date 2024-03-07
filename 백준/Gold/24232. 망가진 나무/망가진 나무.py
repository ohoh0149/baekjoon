import sys
input=sys.stdin.readline
sys.setrecursionlimit(330000)

n=int(input())
graph=[[] for _ in range(n+1)]
direction=[set() for _ in range(n+1)]
edge_dic=dict()
for i in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    direction[u].add(v)
    if u<v:
        edge_dic[(u,v)]=i
    else:
        edge_dic[(v,u)]=i

from collections import deque
parent_lst=[0]*(n+1)
q=deque()
q.append(1)
visited=[0]*(n+1)
visited[1]=1
while q:
    x=q.popleft()
    for nx in graph[x]:
        if visited[nx]==0:
            q.append(nx)
            visited[nx]=1
            parent_lst[nx]=x


dp=[[0,0] for _ in range(n+1)]

def dfs(x):
    global dp
    if dp[x][0]!=0:
        return dp[x][0]

    sm=0
    for nx in graph[x]:
        if parent_lst[x]==nx:
            continue
        sm+=dfs(nx)
        if nx not in direction[x]:
            sm+=1
    dp[x][0]=sm
    return dp[x][0]

dfs(1)
dp[1][1]=dp[1][0]

def dfs2(x):
    if dp[x][1]!=0:
        return dp[x][1]
    p=parent_lst[x]
    temp=dfs2(p)
    if p in direction[x]:
        dp[x][1]=temp-1
    else:
        dp[x][1]=temp+1
    return dp[x][1]

# for i in range(n,0,-1):
#     if dp[i][1]!=0:
#         continue
#     dfs2(i)


q=deque()
q.append(1)
visited=[0]*(n+1)
visited[1]=1
while q:
    x=q.popleft()

    for nx in graph[x]:
        if visited[nx]==0:
            q.append(nx)
            visited[nx]=1
            temp = dp[x][1]
            if x in direction[nx]:
                dp[nx][1] = temp - 1
            else:
                dp[nx][1] = temp + 1





min_num=1
min_val=1e9
for i in range(1,n+1):
    if dp[i][1]<min_val:
        min_val=dp[i][1]
        min_num=i

visited=[0]*(n+1)
q=deque()
q.append(min_num)
visited[min_num]=1
answer=["0"]*(n-1)
while q:
    x=q.popleft()
    for nx in graph[x]:
        if visited[nx]:
            continue
        q.append(nx)
        visited[nx]=1
        if nx not in direction[x]:
            if x<nx:
                answer[edge_dic[(x,nx)]]="1"
            else:
                answer[edge_dic[(nx,x)]]="1"


a="".join(answer)
print(a)