from itertools import product
from copy import deepcopy
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

cctv=[]
wall=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def see(r,c,dir,graph):
    nx=r
    ny=c
    for i in range(max(n,m)):
        # print("nx,ny",nx,ny)
        nx=nx+dx[dir]
        ny=ny+dy[dir]
        if nx>=n or nx<0 or ny>=m or ny <0 or graph[nx][ny]==6:
            break
        else:
            graph[nx][ny]=9



for i in range(n):
    for j in range(m):
        if 1<=graph[i][j]<=5:
            cctv.append(([i,j,graph[i][j]]))
        elif graph[i][j]==6:
            wall.append([i,j])

#print(graph)
#print(cctv)
#print(wall)
def get_result(directions):#(1,1,2,3,4,1)
    temp_graph=deepcopy(graph)
    for i in range(len(cctv)):
        n=cctv[i][2]
        dir=directions[i]
        #print("n",n)
        if n==1:
            see(cctv[i][0],cctv[i][1],dir,temp_graph)
        elif n==2:
            see(cctv[i][0],cctv[i][1],dir,temp_graph)
            see(cctv[i][0],cctv[i][1],(dir+2)%4,temp_graph)
        elif n==3:
            see(cctv[i][0],cctv[i][1],dir,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-1)%4,temp_graph)
        elif n==4:
            see(cctv[i][0],cctv[i][1],dir,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-1)%4,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-2)%4,temp_graph)
        elif n==5:
            see(cctv[i][0],cctv[i][1],dir,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-1)%4,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-2)%4,temp_graph)
            see(cctv[i][0],cctv[i][1],(4+dir-3)%4,temp_graph)
    count=0
    #print(temp_graph)
    for i in temp_graph:
        for j in i:
            if j==0:
                count+=1
    return count


dir_list=list(product([0,1,2,3],repeat=len(cctv)))
#print(dir_list)
result=1e9
for directions in dir_list:#(1,1,3,4...len(cctv))
    temp_result=get_result(directions)
    if result>temp_result:
        result=temp_result


print(result)