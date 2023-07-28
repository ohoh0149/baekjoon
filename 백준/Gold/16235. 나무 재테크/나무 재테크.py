import copy
import sys
input=sys.stdin.readline
def step1():
    global tree_arr
    global y_arr
    for i in range(n):
        for j in range(n):
            l=len(tree_arr[i][j])
            sum_y=0
            new_idx=0
            for idx in range(l-1,-1,-1):
                if y_arr[i][j]<tree_arr[i][j][idx]:
                    sum_y+=tree_arr[i][j][idx]//2
                    if new_idx==0:
                        new_idx=idx+1
                else:
                    y_arr[i][j]-=tree_arr[i][j][idx]
                    tree_arr[i][j][idx]+=1
            if new_idx>=l:
                tree_arr[i][j]=[]
            else:
                tree_arr[i][j]=tree_arr[i][j][new_idx:]
            y_arr[i][j]+=sum_y



dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def step2():
    global tree_arr
    global y_arr
    for i in range(n):
        for j in range(n):
            y_arr[i][j]+=A[i][j]
            for idx,age in enumerate(tree_arr[i][j]):
                if age<5:
                    break
                elif age%5==0:
                    for d in range(8):
                        nx=i+dx[d]
                        ny=j+dy[d]
                        if in_range(nx,ny):
                            tree_arr[nx][ny].append(1)






def print_arr(arr):
    for i in range(n):
        print(*arr[i])
n,m,k=map(int,input().split())
y_arr=[[5]*n for _ in range(n)]
A=[list(map(int,input().split())) for _ in range(n)]
tree_arr=[[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,input().split())
    tree_arr[x-1][y-1].append(z)


for _ in range(k):
    #print("start")
    step1()
    #print_arr(tree_arr)
    #print_arr(y_arr)
    step2()
    #print_arr(tree_arr)
    #print_arr(y_arr)
    #print("end")
result=0
for i in range(n):
    for j in range(n):
        result+=len(tree_arr[i][j])
print(result)
