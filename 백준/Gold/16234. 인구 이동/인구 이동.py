from itertools import combinations
from collections import deque
n,l,r=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def find_united_country():
    global united_country
    visited=[[0]*n for i in range(n)]
    #print("n",n)
    for i in range(n):
        for j in range(n):
            #print(i,j)
            q=deque()
            temp_united=[]
            if visited[i][j]!=0:
                continue
            else:
                
                q.append((i,j))
                #print(q)
                temp_united.append((i,j))
                visited[i][j]=1
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                            if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                                #print("hi")
                                temp_united.append((nx,ny))
                                q.append((nx,ny))
                                visited[nx][ny]=1
            #print(temp_united)
            if len(temp_united)>1:
                united_country.append(temp_united)
    #print(united_country)
                            

count=0
while 1:
    united_country=[]
    find_united_country()
    if len(united_country)==0:
        break
        
    else:
        count+=1
        for i in united_country:
            temp_sum=0
            for j in i:
                temp_sum+=graph[j[0]][j[1]]
            for j in i:
                graph[j[0]][j[1]]=temp_sum//len(i)
                
print(count)