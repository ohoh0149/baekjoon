from collections import defaultdict
from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]

def in_range(x,y):
    return 0<=x<m and 0<=y<n
dx=[0,-1,0,1]
dy=[-1,0,1,0]

size_dic=defaultdict(int)
#near_dic=defaultdict(set)
group_num=0
visited=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j]==0:
            group_num+=1
            q=deque()
            q.append((i,j))
            visited[i][j]=group_num
            count=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0:
                        if not arr[x][y]&(2**d):
                            q.append((nx,ny))
                            visited[nx][ny]=group_num
                            count+=1
            size_dic[group_num]=count



result=0
for i in range(m):
    for j in range(n):
        g1=visited[i][j]
        for d in range(4):
            nx=i+dx[d]
            ny=j+dy[d]
            if in_range(nx,ny) and visited[nx][ny]!=visited[i][j]:
                result=max(result,size_dic[g1]+size_dic[visited[nx][ny]])
                if result==18:
                    print(g1,visited[nx][ny])


print(len(size_dic))
print(max(size_dic.values()))
print(result)

