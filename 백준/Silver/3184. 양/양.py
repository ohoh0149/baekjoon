n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]

from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

visited=[[0]*m for _ in range(n)]
from collections import defaultdict

result_dic=defaultdict(int)

for i in range(n):
    for j in range(m):
        if arr[i][j]=="#" or visited[i][j]!=0:
            continue
        dic = defaultdict(int)
        v_count=0
        o_count=0
        q=deque()
        q.append((i,j))
        visited[i][j]=1
        dic[arr[i][j]]+=1
        while q:
            x,y=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!="#":
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    dic[arr[nx][ny]]+=1
        if dic["o"]>dic["v"]:
            result_dic["o"]+=dic["o"]
        else:
            result_dic["v"]+=dic["v"]


print(result_dic["o"],result_dic["v"])
