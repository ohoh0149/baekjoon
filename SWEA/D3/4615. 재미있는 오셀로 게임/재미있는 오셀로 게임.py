def in_range(x,y):
    return 0<=x<n and 0<=y<n

def check(x,y,d,color):
    while True:
        if arr[x][y]==0:
            return False
        elif arr[x][y]==color:
            return True
        nx=x+dx[d]
        ny=y+dy[d]
        if not in_range(nx,ny):
            return False
        x,y=nx,ny




dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m=map(int,input().split())
    arr=[[0]*n for _ in range(n)]
    arr[n//2-1][n//2-1]=2
    arr[n//2][n//2]=2
    arr[n//2][n//2-1]=1
    arr[n//2-1][n//2]=1

    for _ in range(m):
        c,r,color=map(int,input().split())
        c-=1
        r-=1
        arr[r][c]=color
        for d in range(8):
            nx=r+dx[d]
            ny=c+dy[d]
            if not in_range(nx,ny) or arr[nx][ny]!= 3 - color:
                continue
            flag=check(nx,ny,d,color)
            if flag:
                cx,cy=nx,ny
                for _ in range(n):
                    arr[cx][cy]=color
                    cx=cx+dx[d]
                    cy=cy+dy[d]
                    if arr[cx][cy]==color:
                        break

    count=0
    count2=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                count+=1
            elif arr[i][j]==2:
                count2+=1
    print("#"+str(test_case),count,count2)


    # ///////////////////////////////////////////////////////////////////////////////////
