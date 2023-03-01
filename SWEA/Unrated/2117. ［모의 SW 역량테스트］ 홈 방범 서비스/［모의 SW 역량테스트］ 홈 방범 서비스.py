from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def bfs(r,c,k):
    visited=[[0]*n for _ in range(n)]
    count=0
    q=deque()
    q.append((r,c))
    visited[r][c]=1
    while q:
        x,y=q.popleft()
        if graph[x][y]==1:
            count+=1
        if visited[x][y]==k:
            continue
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
    return count

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////


    result=0
    graph=[]
    n,m= map(int,input().split())
    for i in range(n):
        graph.append(list(map(int,input().split())))

    for k in range(1,22):
        manage_cost=k*k+(k-1)*(k-1)
        for i in range(n):
            for j in range(n):
                c=bfs(i,j,k)
                if m*c-manage_cost>=0:
                    result=max(result,c)

    print("#"+str(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
