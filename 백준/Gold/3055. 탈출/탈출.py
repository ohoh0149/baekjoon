from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<r and 0<=y<c


r,c=map(int,input().split())

#arr=[list(input().split()) for _ in range(r)]
arr=[]
for _ in range(r):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(s)
    arr.append(lst)
#print(arr)

water_pos_lst=[]
water_visited=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        #print(i,j)
        if arr[i][j]=="*":
            water_pos_lst.append((i,j))
            water_visited[i][j]=1
        if arr[i][j]=="S":
            sx,sy=i,j
q=deque(water_pos_lst)
while q:
    x,y=q.popleft()
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and water_visited[nx][ny]==0 and arr[nx][ny] not in ["D","X"]:
            q.append((nx,ny))
            water_visited[nx][ny]=water_visited[x][y]+1

# for i in range(r):
#     print(water_visited[i])


s_visited=[[0]*c for _ in range(r)]
q=deque()
q.append((sx,sy))
s_visited[sx][sy]=1
result=0
while q:
    x,y=q.popleft()
    if arr[x][y]=="D":
        result=s_visited[x][y]-1
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and s_visited[nx][ny]==0 and (water_visited[nx][ny]>s_visited[x][y]+1 or water_visited[nx][ny]==0 )and arr[nx][ny]!="X":
            q.append((nx,ny))
            s_visited[nx][ny]=s_visited[x][y]+1

# for i in range(r):
#     print(s_visited[i])

if result==0:
    print("KAKTUS")
else:
    print(result)