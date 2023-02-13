dx=[0,1,0,-1]
dy=[-1,0,1,0]

graph=[]
n=int(input())
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)

dir=0
temp_obj_count=1
is_two_count=0
count=0
nx,ny=n//2,n//2


result=0
for i in range(n*n-1):
    #print(nx,ny)
    #print(result)
    nx,ny=nx+dx[dir],ny+dy[dir]
    r=(dir+3)%4 #dx[r]dy[r]
    l=(dir+1)%4 #dx[l]dy[l]
    u=(dir+4)%4 #dx[u]dy[u]
    d=(dir+2)%4 #dx[d]dy[d]
    tempdx=[dx[r]+dx[d],dx[l]+dx[d],dx[r],dx[l],dx[r]+dx[r],dx[l]+dx[l],dx[r]+dx[u],dx[l]+dx[u],dx[u]+dx[u],dx[u]]
    tempdy=[dy[r]+dy[d],dy[l]+dy[d],dy[r],dy[l],dy[r]+dy[r],dy[l]+dy[l],dy[r]+dy[u],dy[l]+dy[u],dy[u]+dy[u],dy[u]]
    #print(tempdx,tempdy)
    rest=graph[nx][ny]
    ratio=[1/100,1/100,7/100,7/100,2/100,2/100,10/100,10/100,5/100,0]
    for i in range(10):
        temp_amount=int(graph[nx][ny]*ratio[i])
        if i ==9:
            temp_amount=rest
        tempnx,tempny=nx+tempdx[i],ny+tempdy[i]
        if tempnx<0 or tempnx>=n or tempny<0 or tempny>=n:
            result+=temp_amount
        else:
            graph[tempnx][tempny]+=temp_amount
        rest-=temp_amount
    graph[nx][ny]=0



    count+=1
    if count==temp_obj_count:
        count=0
        dir=(dir+1)%4
        is_two_count+=1
    if is_two_count==2:
        is_two_count=0
        temp_obj_count+=1

print(result)
#print(graph)