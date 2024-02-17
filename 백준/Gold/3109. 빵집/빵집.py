import sys
input = sys.stdin.readline

n,m=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(list(input()))
#print(arr)

dx=[-1,0,1]
result=0
pos_lst=[]
flag=False
def in_range(x,y):
    return 0<=x<n and 0<=y<m
def dfs(x,y):
    global result,pos_lst,arr,flag
    if y==m-1:

        result+=1
        flag=True
        return

    for d in range(3):
        nx=x+dx[d]
        ny=y+1
        if in_range(nx,ny) and arr[nx][ny]=="." :
            arr[nx][ny]="x"
            dfs(nx,ny)
            if flag:
                break

for i in range(n):
    flag=False
    pos_lst=[(i,0)]
    dfs(i,0)

#print(visited)
# for i in range(n):
#     print(arr[i])
print(result)