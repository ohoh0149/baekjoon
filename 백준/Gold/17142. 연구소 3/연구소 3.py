from itertools import combinations
from collections import deque
from copy import deepcopy
n,m =map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)

total_virus=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            graph[i][j]=-1
        elif graph[i][j]==0:
            graph[i][j]=-2
        elif graph[i][j]==2:
            graph[i][j]=-3
            total_virus.append([i,j])
#print(graph)
comb_virus_list=list(combinations(total_virus,m))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def check_nozero_max(arr):
    max_value=0
    for i in arr:
        for j in i:
            if j==-2:
                return 0,max_value
            max_value=max(max_value,j)
            
    return 1,max_value
    
min_count=1e9
for virus_list in comb_virus_list:
    #각 m개당
    count=0
    
    #벽 -1 빈칸 -2 비활성 바이러스 -3
    cur_graph=deepcopy(graph)
    q=deque()
    for i,j in virus_list:
        q.append([i,j,0])
        cur_graph[i][j]=0
    while q:
        x,y,temp_count=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and cur_graph[nx][ny]==-2:
                cur_graph[nx][ny]=cur_graph[x][y]+1
                q.append([nx,ny,temp_count+1])
            elif 0<=nx<n and 0<=ny<n and cur_graph[nx][ny]==-3:
                tc,maxxx=check_nozero_max(cur_graph)
                if tc:
                    
                    min_count=min(min_count,maxxx)
                    #print(cur_graph,maxxx,cur_graph[x][y])
                cur_graph[nx][ny]=cur_graph[x][y]+1
                q.append([nx,ny,temp_count+1])
                
    count=temp_count
    check,maxx=check_nozero_max(cur_graph)
    if check:
        min_count=min(min_count,maxx)

        



if min_count==1e9:
    min_count=-1
print(min_count)
    
    

