import copy
def shark_move(x,y,dir,graph):
    arr=[]
    for i in range(3):
        x=x+dx[dir-1]
        y=y+dy[dir-1]
        if 0<=x<4 and 0<=y<4 and graph[x][y][0]!=0:
            arr.append([x,y])
            
        
    
    return arr


def process(x,y,dir,sum,cur_graph,count):
    #print("sum,count",sum,count)
    global result
    #print("before move",cur_graph)
    fish_move(cur_graph,x,y)
    #print("after move",cur_graph)
    next_shark=shark_move(x,y,dir,cur_graph)
    #print("next_shark",next_shark)
    #print()
    #print()
    if len(next_shark)==0:
        if sum>result:
            result=sum
            return 
    else:
        for tx,ty in next_shark:
            temp_graph=copy.deepcopy(cur_graph)
            temp_graph[tx][ty][0]=0
            dir=temp_graph[tx][ty][1]
            process(tx,ty,dir,sum+cur_graph[tx][ty][0],temp_graph,count+1)
        
    
    
    return
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def fish_move(graph,sharkx,sharky):
    for k in range(1,17):
        k_flag=0
        for i in range(4):
            if k_flag==1:
                break
            for j in range(4):
                if k_flag==1:
                    break
                temp_dir=graph[i][j][1]
                if graph[i][j][0]==k:
                    for l in range(8):
                        nx=i+dx[(temp_dir-1+l)%8]
                        ny=j+dy[(temp_dir-1+l)%8]
                        if 0<=nx<4 and 0<=ny<4 and not (nx==sharkx and ny==sharky):
                            graph[i][j][1]=(temp_dir-1+l)%8+1
                            graph[nx][ny],graph[i][j]=graph[i][j],graph[nx][ny]
                            #print(graph,k)
                            k_flag=1
                            break
                            
                            
                            
                        
                        
                    
                
    return 0


result=0
start_graph=[[]for i in range(4)]
for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4=map(int,input().split())
    start_graph[i].append([a1,b1])
    start_graph[i].append([a2,b2])
    start_graph[i].append([a3,b3])
    start_graph[i].append([a4,b4])
result=start_graph[0][0][0]
start_graph[0][0][0]=0
#print(start_graph)
process(0,0,start_graph[0][0][1],result,start_graph,0)
print(result)
