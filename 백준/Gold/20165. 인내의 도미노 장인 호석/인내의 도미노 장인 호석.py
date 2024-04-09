import copy
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m,r=map(int,input().split())
ori_arr=[list(map(int,input().split())) for _ in range(n)]
def in_range(x,y):
    return 0<=x<n and 0<=y<m

d_dic=dict()
d_dic["N"]=0
d_dic["E"]=1
d_dic["S"]=2
d_dic["W"]=3
arr=copy.deepcopy(ori_arr)
result=0
for _ in range(r):
    #공격
    x,y,d=input().split()
    x=int(x)-1
    y=int(y)-1
    d=d_dic[d]
    #넘어지지 않은 경우에만
    if arr[x][y]!=0:
        h=arr[x][y]
        visited_set=set()
        q=deque()
        q.append((x,y))
        visited_set.add((x,y))
        while q:
            x,y=q.popleft()
            h=arr[x][y]
            for _ in range(h-1):
                x=x+dx[d]
                y=y+dy[d]
                if in_range(x,y) and (x,y) not in visited_set and arr[x][y]>=1:
                    q.append((x,y))
                    visited_set.add((x,y))
        for x,y in visited_set:
            arr[x][y]=0
            result+=1





    #수비
    x,y=map(int,input().split())
    x-=1
    y-=1
    #넘어진 경우에만 세우기
    if arr[x][y]==0:
        arr[x][y]=ori_arr[x][y]


print(result)
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            print("F",end=" ")
        else:
            print("S",end=" ")
    print()