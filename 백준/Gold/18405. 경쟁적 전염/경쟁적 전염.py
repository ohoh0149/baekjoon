from collections import deque
from itertools import combinations
import copy
import sys
input= sys.stdin.readline

n,k=map(int, input().split())
graph=[[0]*(n+1)]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))
#print(graph)
s,x,y=map(int,input().split())

q=deque()
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]!=0:
            q.append((graph[i][j],0,i,j))

q=deque(sorted(q))
#print(q)
count=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
while q:
    virus_num,time,tx,ty=q.popleft()
    if time==s:
        break
    for i in range(4):
        nx=tx+dx[i]
        ny=ty+dy[i]
        if 1<=nx<=n and 1<=ny<=n and graph[nx][ny]==0:
            graph[nx][ny]=virus_num
            q.append((virus_num,time+1,nx,ny))
print(graph[x][y])
    