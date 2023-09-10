
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n
def dfs(k,x,y,used):
    global cur_max
    cur_max=max(k,cur_max)
    if k==21:
        cur_max=max(cur_max,k)
        return
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if in_range(nx,ny) and visited[nx][ny]==0:
            if arr[nx][ny]<arr[x][y]:
                visited[nx][ny]=1
                dfs(k+1,nx,ny,used)
                visited[nx][ny]=0
            else:
                if arr[nx][ny]-ki<arr[x][y] and used==0:
                    visited[nx][ny]=1
                    temp=arr[nx][ny]
                    arr[nx][ny]=arr[x][y]-1
                    dfs(k+1,nx,ny,1)
                    arr[nx][ny]=temp
                    visited[nx][ny]=0


cur_max=0
def get_max(sx,sy):
    global cur_max
    for i in range(n):
        for j in range(n):
            visited[i][j]=0
    cur_max=0
    visited[sx][sy]=1
    dfs(0,sx,sy,0)


    return cur_max


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,ki=map(int,input().split())
    visited=[[0]*n for _ in range(n)]
    arr=[list(map(int,input().split())) for _ in range(n)]
    top=0

    for i in range(n):
        top=max(top,max(arr[i]))

    result=0
    top_lst=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==top:
                top_lst.append((i,j))
    for x,y in top_lst:

        get_max(x,y)
        result=max(result,cur_max)
    print("#"+str(test_case),result+1)


    # ///////////////////////////////////////////////////////////////////////////////////
