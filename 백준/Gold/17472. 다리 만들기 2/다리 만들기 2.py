from collections import deque
from itertools import combinations
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

land_arr=[[0]*m for _ in range(n)]

def print_arr(arr):
    for i in range(n):
        print(arr[i])
#각 섬별로 1번섬~ r번 섬까지 나타내기
land_num=0
for i in range(n):
    for j in range(m):
        if land_arr[i][j]==0 and arr[i][j]==1:
            land_num+=1
            q=deque()
            q.append((i,j))
            land_arr[i][j]=land_num
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and land_arr[nx][ny]==0 and arr[nx][ny]==1:
                        q.append((nx,ny))
                        land_arr[nx][ny]=land_num

#print_arr(land_arr)
#print(land_num)
r=land_num
bridge_arr=[[9]*(r+1) for _ in range(r+1)]
#print(bridge_arr)


##다리 구해보자

# 먼저 가로 다리 부터
for i in range(n):
    count=0
    for j in range(1,m):
        if arr[i][j]==0:
            count+=1
        else:
            #다리 발견!
            if count>=2 and arr[i][j-count-1]==1:
                a,b=land_arr[i][j-count-1],land_arr[i][j]
                # print("bridge")
                # print(i,j-count-1,i,j)
                # print(a,b,count)
                if a!=b:
                    bridge_arr[a][b]=min(bridge_arr[a][b],count)
                    bridge_arr[b][a]=min(bridge_arr[b][a],count)
            count=0

#세로 다리
for j in range(m):
    count=0
    for i in range(1,n):
        if arr[i][j]==0:
            count+=1
        else:
            #다리 발견!
            if count>=2 and arr[i-count-1][j]==1:
                a,b=land_arr[i-count-1][j],land_arr[i][j]
                # print("bridge")
                # print(i,j-count-1,i,j)
                # print(a,b,count)
                if a!=b:
                    bridge_arr[a][b]=min(bridge_arr[a][b],count)
                    bridge_arr[b][a]=min(bridge_arr[b][a],count)
            count=0
#
# for i in range(n):
#     print(land_arr[i])
# for i in range(1,r+1):
#     print(bridge_arr[i][1:])

lst=[]
for i in range(1,r+1):
    for j in range(i+1,r+1):
        if bridge_arr[i][j]!=9:
            lst.append((i,j))
#print(lst)



comb_lst=list(combinations(lst,r-1))
#print(comb_lst)

result=1e9
for comb in comb_lst:
    #print(comb)
    s=set()
    for a,b in comb:
        s.add(a)
        s.add(b)
    if len(s)==r:
        temp_graph=[[0]*(r+1) for _ in range(r+1)]
        for a,b in comb:
            temp_graph[a][b]=1
            temp_graph[b][a]=1
        q=deque()
        q.append(1)
        visited=[0]*(r+1)
        visited[1]=1
        while q:
            x=q.popleft()
            for v in range(1,r+1):
                if temp_graph[x][v]==1 and visited[v]==0:
                    q.append(v)
                    visited[v]=1
        if sum(visited)!=r:
            continue


        temp_result=0
        for a,b in comb:
            temp_result+=bridge_arr[a][b]
        result=min(result,temp_result)


if result==1e9:
    print(-1)
else:
    print(result)

