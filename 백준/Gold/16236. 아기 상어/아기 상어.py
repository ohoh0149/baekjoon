from collections import deque

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)
sharki=0
sharkj=0
fish_arr=[]
for i in range(n):
    for j in range(n):
        if 1<=graph[i][j]<=6:
            fish_arr.append(((i,j),graph[i][j]))
        if graph[i][j]==9:
            sharki,sharkj=i,j
            graph[i][j]=0

#print(fish_arr)
cur_fish_index=0
fish_arr.sort(key=lambda x: x[1])
#print(fish_arr)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

shark_size=2
size_level=0
result=0
count=0
while 1:

    if len(fish_arr)==0 or fish_arr[0][1]>=shark_size  :
        break

    else:
        #eat 실행 
        #print(result)
        visited=[[-1]*n for i in range(n)]
        q=deque()
        q.append((sharki,sharkj,0))
        visited[sharki][sharkj]=0
        choose=[]
        while q:
           #print("QQ")
            tempi,tempj,templen=q.popleft()
            #print(tempi,tempj,templen)
            for i in range(4):
                nx=tempi+dx[i]
                ny=tempj+dy[i]
                
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and graph[nx][ny]<=shark_size:
                    if graph[nx][ny]!=0 and graph[nx][ny]<shark_size:
                        choose.append((nx,ny,templen+1))
                    
                    q.append((nx,ny,templen+1))
                    visited[nx][ny]=templen+1
        if len(choose)==0:
            break
        choose.sort(key=lambda x:x[1])
        choose.sort(key=lambda x:x[0])
        choose.sort(key=lambda x:x[2])
        #print("choose",choose)
        #print("result",result)
        sharki=choose[0][0]
        sharkj=choose[0][1]
        #print(sharki,sharkj)
        graph[sharki][sharkj]=0
        size_level+=1
        result+=choose[0][2]
        
        for i in fish_arr:
            if i[0]==(sharki,sharkj):
                #print(sharki,sharkj)
                #print("testjslekjtlskejtlksejtlksejtlset")
                #print(fish_arr)
                fish_arr.remove(i)
                #print(fish_arr)
        if size_level==shark_size:
            size_level=0
            shark_size+=1
            #print(shark_size)
        #cur_fish_index+=1
print(result)
            
            
        
        
        
        