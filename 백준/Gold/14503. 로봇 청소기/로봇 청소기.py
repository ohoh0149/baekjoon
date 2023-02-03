n,m= map(int,input().split())
r,c,d=map(int,input().split())
graph=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    graph.append(list(map(int,input().split())))

#print(graph)


tempr=r
tempc=c
tempd=d
#(4+d)%4
result=0
while 1:
    flag=0
    #print(result)
    if graph[tempr][tempc]!=2:
        graph[tempr][tempc]=2
        result+=1
    for i in range(4):
        dir=(4+tempd-i-1)%4
        nx=tempr+dx[dir]  
        ny=tempc+dy[dir]
        if graph[nx][ny]==0:
            tempr=nx
            tempc=ny
            tempd=dir
            flag=1
            break
    if flag!=1:
        tempr=tempr-dx[dir]
        tempc=tempc-dy[dir]
        if graph[tempr][tempc]==1:
            break
            

print(result)