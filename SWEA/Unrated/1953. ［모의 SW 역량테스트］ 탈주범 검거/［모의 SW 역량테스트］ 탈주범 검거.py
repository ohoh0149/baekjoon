from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    n,m,r,c,l=map(int,input().split())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))

    #print(graph)

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    dok=[[1,2,5,6],[1,3,6,7],[1,2,4,7],[1,3,4,5]]
    dcur=[[0],[0,1,2,3],[0,2],[1,3],[0,1],[1,2],[2,3],[0,3]]
    visited=[[0]*m for i in range(n)]
    q=deque()
    q.append((r,c))
    visited[r][c]=1
    count=1
    while q:
        x,y=q.popleft()
        if visited[x][y]==l:
            continue
        for i in range(4):
            if i not in dcur[graph[x][y]]:
                continue
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and (graph[nx][ny] in dok[i]):
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
                
                count+=1
    print("#"+str(test_case),count)

    # ///////////////////////////////////////////////////////////////////////////////////
