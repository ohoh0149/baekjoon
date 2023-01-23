from collections import deque
from itertools import combinations
import copy
import sys
input= sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def virus(temp_graph):
    q=deque()
    #print(virus_list)
    for a,b in virus_list:
        q.append((a,b))
    while q:
        x,y=q.popleft()
        temp_graph[x][y]=2
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and temp_graph[nx][ny]==0:
                q.append((nx,ny))
                #print("nx ny ",nx,ny)
    #print("in virus temp_graph",temp_graph)
        
    
    
def count_0(temp_graph):
    #print("incount0 graph",temp_graph)
    count=0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j]==0:
                count+=1
    return count


    

arr=[]
virus_list=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            arr.append((i,j))
        if graph[i][j]==2:
            virus_list.append((i,j))
comb=list(combinations(arr,3))
#print(comb)
max=0
flag=0
for a in comb:
    
    # if flag==10:
    #     break
    temp_graph=copy.deepcopy(graph)
    temp_graph[a[0][0]][a[0][1]]=1
    temp_graph[a[1][0]][a[1][1]]=1
    temp_graph[a[2][0]][a[2][1]]=1
    
    virus(temp_graph)
    # if flag==0:
    #     print(temp_graph)
    # flag+=1
    temp=count_0(temp_graph)
    #print(temp)
    if temp>max:
        max=temp
print(max)
        