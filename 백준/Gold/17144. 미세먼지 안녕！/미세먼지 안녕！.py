import copy


r,c,t=map(int,input().split())
graph=[]
for i in range(r):
    graph.append(list(map(int,input().split())))
#print(graph)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def spread(graph):
    new_graph=[[0]*c for i in range(r)]
    new_graph[clean_air[0][0]][0]=-1
    new_graph[clean_air[1][0]][0]=-1
    for i in range(r):
        for j in range(c):
            if graph[i][j]==0 or graph[i][j]==-1:
                continue
            spread_amount=graph[i][j]//5
            spread_count=0
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                if  0<=nx<r and 0<=ny<c and graph[nx][ny]!=-1:
                    spread_count+=1
                    new_graph[nx][ny]+=spread_amount
            new_graph[i][j]+=graph[i][j]-spread_count*spread_amount
            #print("spraed_coutn",spread_count)
            #print('newgraph[i][j]',new_graph[i][j],i,j)
    #print(new_graph)
    return new_graph

clean_air=[]
for i in range(r):
    for j in range(c):
        if graph[i][j]==-1:
            clean_air.append((i,j))
#print(clean_air)
def get_next_area(i,j,sign):
    if sign==1:#up
        if j==0 and i!=clean_air[0][0]:
            return i+1,j
        elif i==0 and j!=0:
            return i,j-1
        elif j==c-1 and i!=0:
            return i-1,j
        elif i==clean_air[0][0] and j!=c-1:
            return i,j+1
    if sign==2:#down
        if i==clean_air[1][0] and j!=c-1:
            return i,j+1
        elif j==c-1 and i!=r-1:
            return i+1,j
        elif i==r-1 and j!=0:
            return i,j-1
        elif j==0 and i>clean_air[1][0]:
            return i-1,j

#clean_air=[(2,0),(3,0)]
def run_clean_air(graph):
    up_r=clean_air[0][0]
    down_r=clean_air[1][0]
    graph[up_r-1][0]=-1
    graph[up_r][0]=0
    graph[down_r][0]=0
    graph[down_r+1][0]=-1
    sign=1
    new_graph=copy.deepcopy(graph)
    for i in range(up_r+1):
        for j in range(c):
            if i==0 or i==up_r or j==0 or j==c-1:
                nx,ny=get_next_area(i,j,1)
                new_graph[nx][ny]=graph[i][j]
    for i in range(down_r,r):
        for j in range(c):
            if i==down_r or i==r-1 or j==0 or j==c-1:
                nx,ny=get_next_area(i,j,2)
                new_graph[nx][ny]=graph[i][j]
    return new_graph
    # for col in range(1,c):
    #     nx,ny=get_next_area(up_r,col,1)
    #     graph[nx][ny]=graph[up_r][col]
    # for row in range(up_r-1,-1,-1):
    #     nx,ny=get_next_area(row,c-1,sign)
    #     graph[nx][ny]=graph[row][c-1]
    # for col in range(c-2,-1,-1):
    #     nx,ny=get_next_area(0,col,sign)
    #     graph[nx][ny]=graph[0][]
    sign=2
    

    
#print(spread(graph))
for i in range(t):
    graph=spread(graph)
    #print(graph)
    graph=run_clean_air(graph)
    #print(graph)

sum=0
for i in range(r):
    for j in range(c):
        if graph[i][j]>0:
            sum+=graph[i][j]
print(sum)