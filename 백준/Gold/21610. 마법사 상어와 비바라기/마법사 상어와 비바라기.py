import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

move=[]
for i in range(m):
    a,b=map(int,input().split())
    move.append((a,b))
#print(graph)
#print(move)
dx=[None,0,-1,-1,-1,0,1,1,1]
dy=[None,-1,-1,0,1,1,1,0,-1]
clouds=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for ds in move:
    visited=[[0]*n for i in range(n)]
    d=ds[0]
    s=ds[1]
    for cloud in clouds:
        cloud[0]=(cloud[0]+s*dx[d]+n)%n
        cloud[1]=(cloud[1]+s*dy[d]+n)%n
        graph[cloud[0]][cloud[1]]+=1
        visited[cloud[0]][cloud[1]]=1
    for cloud in clouds:
        count=0
        for i in range(2,9,2):
            nx=cloud[0]+dx[i]
            ny=cloud[1]+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                count+=1
        graph[cloud[0]][cloud[1]]+=count
    
    clouds=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2 and visited[i][j]==0:
                clouds.append([i,j])
                graph[i][j]-=2
    #print(graph)

sum=0
for i in range(n):
        for j in range(n):
            sum+=graph[i][j]
print(sum)

    

