from collections import deque
dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]
while True:
    l,r,c=map(int,input().split())
    def print_arr(arr):
        for i in range(l):
            for j in range(r):
                print(arr[i][j])
            print()
        print()

    if l==0:
        break
    def in_range(x,y,z):
        return 0<=x<l and 0<=y<r and 0<=z<c

    arr=[]
    for _ in range(l):
        temp_arr=[list(input()) for _ in range(r)]
        input()
        arr.append(temp_arr)


    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k]=="S":
                    sx,sy,sz=i,j,k
                if arr[i][j][k]=="E":
                    ex,ey,ez=i,j,k

    visited=[[[0]*c for _ in range(r)] for _ in range(l)]
    q=deque()
    q.append((sx,sy,sz))
    visited[sx][sy][sz]=1
    result=0
    while q:
        x,y,z=q.popleft()
        if x==ex and y==ey and z==ez:
            result=visited[x][y][z]-1
            break

        for d in range(6):
            nx=x+dx[d]
            ny=y+dy[d]
            nz=z+dz[d]
            if in_range(nx,ny,nz) and visited[nx][ny][nz]==0 and arr[nx][ny][nz] in ["." ,"E"]:
                q.append((nx,ny,nz))
                visited[nx][ny][nz]=visited[x][y][z]+1

    if result==0:
        print("Trapped!")
    else:
        print("Escaped in",result,"minute(s).")




