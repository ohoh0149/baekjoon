from collections import deque
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)
def showgraph(graph):
    for i in range(n):
        print(graph[i])

# for i in range(n-1,-1,-1):
#     print("i",i)
# exit()

def move(graph):
    #ret_arr=[[-2]*n for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(n):
            #print(i,j)
            if graph[i][j]==-2 or graph[i][j]==-1:
                continue
            nx,ny=i,j
            for k in range(n):
                if (nx+1)>=n:
                    break
                if graph[nx+1][ny]>=-1:
                    break
                nx=nx+1
            if nx!=i:    
                graph[nx][ny]=graph[i][j]
                graph[i][j]=-2
    return graph

# print(move([[2, 2, -1, 3, 1], [-2, -2, 2, 0, -1], [-2, -2, -2, 1, 2], [-1, -2, 1, 3, 2], [-2, -2, 2, 2, 1]]))

# exit()
def rotate(arr):
    ret_arr=[[-2]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ret_arr[n-1-j][i]=arr[i][j]
    return ret_arr



dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(i,j,check_graph):
    del_list=[]
    del_list.append((i,j))
    check_graph[i][j]=1
    temp_count=1
    temp_rain_count=0
    visited=[[0]*n for i in range(n)]
    color=graph[i][j]
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                if graph[nx][ny]==color:
                    check_graph[nx][ny]=1
                    temp_count+=1
                    q.append((nx,ny))
                    del_list.append((nx,ny))
                elif graph[nx][ny]==0:
                    q.append((nx,ny))
                    del_list.append((nx,ny))
                    temp_count+=1
                    temp_rain_count+=1
                else:
                    continue


    return temp_count,temp_rain_count,del_list

# check_graph=[[0]*n for i in range(n)]
# print(bfs(1,1,check_graph))
# exit()
result=0
while True:
    maxcount=0
    maxr=0
    maxc=0
    max_raincount=0
    real_del_list=[]
    check_graph=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]<=0 or check_graph[i][j]==1:
                continue
            count,raincount,del_list=bfs(i,j,check_graph)
            
            if count>maxcount:
                maxcount=count
                max_raincount=raincount
                maxr=i
                maxc=j
                real_del_list=del_list
            elif count==maxcount:
                if raincount>=max_raincount:
                    maxcount=count
                    max_raincount=raincount
                    maxr=i
                    maxc=j
                    real_del_list=del_list
    if maxcount<2:
        break
    else:
        #2
        #print("----------------------")
        #showgraph(graph)
        for i,j in real_del_list:
            graph[i][j]=-2
        result+=maxcount**2
        #print(maxcount)
        #print(real_del_list)
        #print(result)
        
        #3
        graph=move(graph)
        
        #4
        graph=rotate(graph)
        
        graph=move(graph)
       # print("000000000009090909")
        #showgraph(graph)

        #print("------------------------")
        
        #5

    
        
print(result)                


