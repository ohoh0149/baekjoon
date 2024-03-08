arr=[list(map(int,input().split())) for _ in range(5)]

s=set()
def in_range(x,y):
    return 0<=x<5 and 0<=y<5

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y,cur,k):
    global s
    if k==6:
        s.add(cur)
        return
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny):
            dfs(nx,ny,cur+str(arr[nx][ny]),k+1)

for i in range(5):
    for j in range(5):
        dfs(i,j,"",0)

print(len(s))


