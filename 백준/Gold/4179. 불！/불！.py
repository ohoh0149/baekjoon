from collections import deque
r,c=map(int,input().split())

def in_range(x,y):
    return 0<=x<r and 0<=y<c

arr=[]
for _ in range(r):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(s)
    arr.append(lst)
#print(arr)

f_lst=[]
jr,jc=0,0
for i in range(r):
    for j in range(c):
        if arr[i][j]=="F":
            f_lst.append((i,j))
        elif arr[i][j]=="J":
            jr,jc=i,j

q=deque()

#visited=[[0]*c for _ in range(r)]
for fx,fy in f_lst:
    q.append((fx,fy,0))
    #visited[fx][fy]=1
q.append((jr,jc,0))

result=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
while q:
    x,y,time=q.popleft()
    if result!=0:
        break
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and arr[nx][ny]==".":
            q.append((nx,ny,time+1))
            arr[nx][ny]=arr[x][y]
        if not in_range(nx,ny) and arr[x][y]=="J":
            result=time+1
            break



if result==0:
    print("IMPOSSIBLE")
else:
    print(result)

