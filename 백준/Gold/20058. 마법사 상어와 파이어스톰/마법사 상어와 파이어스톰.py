import copy
from collections import deque
n,q=map(int,input().split())
arr=[]
for i in range(2**n):
    arr.append(list(map(int,input().split())))
li=list(map(int,input().split()))

count=1
# for i in range(2**n):
#     for j in range(2**n):
#         arr[i][j]=count
#         count+=1
# print(graph)
def rotate90(r1,c1,l):
    r2=r1+2**l-1
    c2=c1+2**l-1
    #print("r",r1,c1,r2,c2)
    for i in range(2**(l-1)):
        for j in range(i,(2**l)-1-i):
            #print(i,j)
            #print(arr[r1+i][c1+j],arr[r1+j][c2-i],arr[r2-i][c2-j],arr[r2-j][c1+i])
            arr[r1+i][c1+j],arr[r1+j][c2-i],arr[r2-i][c2-j],arr[r2-j][c1+i]=arr[r2-j][c1+i],arr[r1+i][c1+j],arr[r1+j][c2-i],arr[r2-i][c2-j]
    #print(arr)


dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(q):
    l=li[i]
    for i in range(0,2**n,2**l):
        for j in range(0,2**n,2**l):
            #print(i,j)
            if l!=0:
                rotate90(i,j,l)
    arr2=copy.deepcopy(arr)
    for i in range(2**n):
        for j in range(2**n):
            count=0
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                if 0<=nx<2**n and 0<=ny<2**n and arr2[nx][ny]>=1:
                    count+=1
            if count<3 and arr[i][j]>0:
                arr[i][j]-=1
sum=0

max_value=0
visited=[[0]*(2**n) for i in range(2**n)]
#print(visited)
for i in range(2**n):
    for j in range(2**n):
        #print(i,j)
        link=0
        if visited[i][j]==0 and arr[i][j]>0:
            q=deque()
            q.append([i,j])
            visited[i][j]=1
            link+=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    ni=x+dx[d]
                    nj=y+dy[d]
                    if 0<=ni<2**n and 0<=nj<2**n and arr[ni][nj]>0 and visited[ni][nj]==0:
                        visited[ni][nj]=1
                        link+=1
                        q.append([ni,nj])
            max_value=max(max_value,link)
            

for i in range(2**n):
    for j in range(2**n):
        sum+=arr[i][j]
print(sum)
print(max_value)