from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def get_result():
    visited=[[0]*m for _ in range(n)]
    q=deque()
    for vx,vy in virus_lst:
        q.append((vx,vy))
        visited[vx][vy]=1
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0 and visited[i][j]==0:
                count+=1
    return count



n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

virus_lst=[]
zero_lst=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            virus_lst.append((i,j))
        elif arr[i][j]==0:
            zero_lst.append((i,j))

case_lst=list(combinations(zero_lst,3))
result=0
for case in case_lst:
    for x,y in case:
        arr[x][y]=1
    result=max(result,get_result())
    for x,y in case:
        arr[x][y]=0




print(result)

