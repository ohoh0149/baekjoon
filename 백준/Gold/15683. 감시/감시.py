from itertools import product

def in_range(x,y):
    return 0<=x<n and 0<=y<m

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

cctv_lst=[]
for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            cctv_lst.append((i,j))
d_lst=[[0],[0],[0,2],[0,1],[0,1,2],[0,1,2,3]]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=1e9
case_lst=list(product([0,1,2,3] ,repeat=len(cctv_lst)))
for case in case_lst:
    visited=[[0]*m for _ in range(n)]
    #case = [ 0, 3, 1 , 3 ,...cctv len]
    for idx,d in enumerate(case):
        ax,ay=cctv_lst[idx]
        #print(ax,ay)
        for cur_d in d_lst[arr[ax][ay]]:
            x, y = ax,ay
            visited[x][y]=1
            rd=(cur_d+d)%4
            for _ in range(max(n,m)):
                x=x+dx[rd]
                y=y+dy[rd]
                if not in_range(x,y) or arr[x][y]==6:
                    break
                else:
                    visited[x][y]=1
    #print(visited)
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0 and visited[i][j]==0:
                count+=1
    result=min(count,result)

print(result)







