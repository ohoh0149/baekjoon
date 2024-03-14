



visited=[]
n=0
from collections import deque
import heapq
def in_range(x,y):
    return 0<=x<n and 0<=y<n
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def solution(board):
    global n,visited
    n=len(board)
    visited=[[[-1]*4 for _ in range(n)] for _ in range(n)]

    
    for d in range(4):
        visited[0][0][d]=0
    
    q=[]
    #q.append((0,0,-1))
    heapq.heappush(q,(0,0,0,-1))
    result=1e9
    while q:
        cost,x,y,bd=heapq.heappop(q)
        if visited[x][y][bd]>=result:
            continue
        if x==n-1 and y==n-1:
            result=min(result,visited[n-1][n-1][bd])
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if not in_range(nx,ny) or board[nx][ny]==1:
                continue
            if d==bd or (x==0 and y==0):
                cost=100
            else:
                cost=600
            if visited[nx][ny][d]>=visited[x][y][bd]+cost or visited[nx][ny][d]==-1:
                visited[nx][ny][d]=visited[x][y][bd]+cost
                #q.append((nx,ny,d))
                heapq.heappush(q,(visited[nx][ny][d],nx,ny,d))

            
            

    # for i in range(n):
    #     print(visited[i])
    min_val=1e9
    for val in visited[n-1][n-1]:
        if val!=-1:
            min_val=min(min_val,val)

    return min_val