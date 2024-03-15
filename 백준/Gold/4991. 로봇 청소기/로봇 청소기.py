from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
    m,n=map(int,input().split())
    if m==0:
        break
    arr=[list(input()) for _ in range(n)]
    def in_range(x,y):
        return 0<=x<n and 0<=y<m

    def get_length(x1,y1,x2,y2):
        q=deque()
        visited=[[0]*m for _ in range(n)]
        visited[x1][y1]=1
        q.append((x1,y1))
        while q:
            x,y=q.popleft()
            if x==x2 and y==y2:
                return visited[x][y]-1
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!="x":
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
        return -1
    pos_lst=[]
    for i in range(n):
        for j in range(m):
            if arr[i][j]=="*":
                pos_lst.append((i,j))
            elif arr[i][j]=="o":
                sx,sy=i,j
                arr[i][j]="."

    l=len(pos_lst)
    visited=[0]*l
    result=1e9
    dic=dict()
    def dfs(k,cur_length,bx,by):
        global result,dic
        if cur_length>=result:
            return
        if k==l:
            result=min(result,cur_length)
            return

        for i in range(l):
            if visited[i]==0:
                visited[i]=1
                cx,cy=pos_lst[i]
                if (bx,by,cx,cy) not in dic:
                    g=get_length(bx,by,cx,cy)
                    dic[(bx,by,cx,cy)]=g
                    dic[(cx,cy,bx,by)]=g
                else:
                    g=dic[(bx,by,cx,cy)]
                if g!=-1:
                    dfs(k+1,cur_length+g,cx,cy)
                visited[i]=0

    dfs(0,0,sx,sy)
    if result==1e9:
        print(-1)
    else:
        print(result)