from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def solution(land):
    answer = 0
    n=len(land)
    m=len(land[0])
    def in_range(x,y):
        return 0<=x<n and 0<=y<m

    visited=[[0]*m for _ in range(n)]
    group_num=0
    dic=dict()
    for i in range(n):
        for j in range(m):
            if land[i][j]==0 or visited[i][j]!=0:
                continue
            q=deque()
            q.append((i,j))
            group_num+=1
            visited[i][j]=group_num
            count=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0 and land[nx][ny]==1: 
                        q.append((nx,ny))
                        visited[nx][ny]=group_num
                        count+=1
            dic[group_num]=count
    # for i in range(n):
    #     print(land[i])
    # for i in range(n):
    #     print(visited[i])
    # print(dic)
    
    for j in range(m):
        s=set()
        for i in range(n):
            if visited[i][j]>0:
                s.add(visited[i][j])
        result=0
        for a in s:
            result+=dic[a]
        answer=max(result,answer)
            
            
    return answer