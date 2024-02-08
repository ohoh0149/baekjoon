r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input()))
#print(arr)

result=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c

a_visited=[0]*200
a_visited[ord(arr[0][0])]=1
def dfs(k,x,y):
    global result,a_visited
    if result==26:
        return
    result=max(result,k+1)
    if k==25:
        return
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and a_visited[ord(arr[nx][ny])]==0:
            a_visited[(ord(arr[nx][ny]))]=1
            dfs(k+1,nx,ny)
            a_visited[(ord(arr[nx][ny]))]=0

dfs(0,0,0)
print(result)



# r,c=map(int,input().split())
# arr=[]
# for _ in range(r):
#     arr.append(list(input()))
#
# from collections import deque
# visited=[[0]*c for _ in range(r)]
# #[[k,set],[k,set]....]
