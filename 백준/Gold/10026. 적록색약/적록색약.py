from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def get_result1():
    count=0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=0:
                continue
            count+=1
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==arr[x][y]:
                        q.append((nx,ny))
                        visited[nx][ny]=1
    return count



def get_result2():
    return 0
n=int(input())
arr=[]
for _ in range(n):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(s)
    arr.append(lst)

result1=get_result1()
for i in range(n):
    for j in range(n):
        if arr[i][j]=="R":
            arr[i][j]="G"
result2=get_result1()

print(result1,result2)
