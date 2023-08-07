


from collections import deque



dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check_zero(x,y,t):
    if arr[x][y]!="0"and arr[x][y]!="E" and arr[x][y]!="B":
        return False
    for i in range(2):
        nx=x+dx[t*2+i]
        ny=y+dy[t*2+i]
        #print("nx,ny")
        #print(nx,ny)
        if arr[nx][ny]!="0"and arr[nx][ny]!="E" and arr[nx][ny]!="B":
            return False
    return True


def check_find(x,y,t):
    if arr[x][y]!="E":
        return False
    for i in range(2):
        nx=x+dx[t*2+i]
        ny=y+dy[t*2+i]
        if arr[nx][ny]!="E":
            return False
    return True


def in_range(x,y):
    return 1<=x<=n and 1<=y<=n


def bfs(x,y,t):
    q=deque()
    visited=[[[0]*2 for _ in range(n+1)] for _ in range(n+1)]
    visited[x][y][t]=1
    q.append((x,y,t))
    result=0
    while q:

        x,y,t=q.popleft()
        for d in range(5):
            if d==4:
                isfail=False
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        #print(x + a, y + b)
                        if arr[x + a][y + b] == "1":
                            isfail=True
                            break
                    if isfail:
                        break
                if isfail:
                    continue
                nx=x
                ny=y
                nt=(t+1)%2
            else:

                nx=x+dx[d]
                ny=y+dy[d]
                nt=t
            #nx,ny,t 에 대해서 탐색
            #정답인지 체크하자 먼저
            #print(nx,ny,nt)
            if check_find(nx,ny,nt):

                result=visited[x][y][t]
                #print("result",result)
                break

            if in_range(nx,ny) and visited[nx][ny][nt]==0 and check_zero(nx,ny,nt):
                q.append((nx,ny,nt))
                visited[nx][ny][nt]=visited[x][y][t]+1
                #print("ok",nx,ny,nt)
                #print(visited[nx][ny][nt])


        if result!=0:
            break

    return result




n=int(input())
arr=[]
arr.append("1"*(n+1))
for _ in range(n):
    arr.append("1"+input()+"1")
arr.append("1"*(n+1))
tem=0
sx,sy=-1,-1
t=-1
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]=="B":
            tem+=1
            if tem==2:
                sx,sy=i,j
                if arr[i][j+1]=="B":
                    t=1
                else:
                    t=0
                break
    if sx!=-1:
        break
#print(sx,sy,t)
print(bfs(sx,sy,t))






