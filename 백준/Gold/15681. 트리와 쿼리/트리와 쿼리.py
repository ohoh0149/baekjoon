import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n,r,qq=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

from collections import deque
visited=[0]*(n+1)
q=deque()
visited[r]=1
q.append(r)

# 부모,[자식들]
tree=[0]*(n+1)
for i in range(1,n+1):
    tree[i]=[0,[]]

while q:
    x=q.popleft()
    for nx in graph[x]:
        if not visited[nx]:
            tree[x][1].append(nx)
            tree[nx][0]=x
            visited[nx]=visited[x]+1
            q.append(nx)
#print(visited)
#print(tree)

visited=[0]*(n+1)

def dfs(num):
    global visited
    if visited[num]:
        return visited[num]
    sm=1
    for c in tree[num][1]:
        sm+=dfs(c)
    visited[num]=sm
    return sm



# def get_answer(num):
#     q=deque()
#     q.append(num)
#     count=1
#     while q:
#         x=q.popleft()
#         for nx in graph[x]:
#             if visited[nx]>visited[x]:
#                 q.append(nx)
#                 count+=1
#     return count
#
#

dfs(r)
for _ in range(qq):
    u=int(input())
    print(visited[u])