def catch_shark(col):
    global result
    for i in range(1,r+1):
        if arr[i][col]==0:
            continue
        else:
            result+=arr[i][col][2]
            arr[i][col]=0
            break

def in_range(x,y):
    if 1<=x<=r and 1<=y<=c:
        return True
    else:
        return False

def invert_d(d):
    if d==1 or d==3:
        d+=1
    elif d==2 or d==4:
        d-=1
    else:
        print("error!")
    return d



dx=[0,-1,1,0,0]
dy=[0,0,0,1,-1]
def move_shark():
    global arr
    new_arr=[[0]*(c+1) for _ in range(r+1)]
    for i in range(1,r+1):
        for j in range(1,c+1):
            #상어가 없으면 컨티뉴
            if arr[i][j]==0:
                continue
            else:
                #현재 위치
                x,y=i,j
                s=arr[i][j][0]
                d= arr[i][j][1]
                z=arr[i][j][2]
                if d==1 or d==2:
                    new_s=s%((r-1)*2)
                else:
                    new_s=s%((c-1)*2)
                #속력만큼 반복하면서 이동해주기
                for k in range(new_s):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    #범위 밖인 경우 좌표 변경 , 방향 반대
                    if not in_range(nx,ny):
                        d=invert_d(d)
                        arr[i][j][1]=d
                        nx=x+dx[d]
                        ny=y+dy[d]
                    x=nx
                    y=ny

                #최종 좌표(x,y)에 대해서 겹치는지 안겹치는 지 따져야 한다.
                if new_arr[x][y]==0:
                    new_arr[x][y]=[s,d,z]
                #상어가 겹치는 경우 크기가 큰녀석이 이김
                else:
                    #원래 있던애가 큰경우
                    if new_arr[x][y][2]>z:
                        continue
                    #현재 있던 애가 큰 경우 현재 녀석으로 교체
                    else:
                        new_arr[x][y]=[s,d,z]
    arr=new_arr













r,c,m=map(int,input().split())
result=0
arr=[[0]*(c+1) for _ in range(r+1)]
for i in range(m):
    x,y,s,d,z=map(int,input().split())
    arr[x][y]=[s,d,z]
#print(arr)
def print_arr(arr):
    for i in range(1,r+1):
        print(arr[i][1:])
#catch_shark(2)
#print_arr(arr)
#
for j in range(1,c+1):
    catch_shark(j)
    #print("after catch",j)
    #print_arr(arr)
    move_shark()
    #print("after move")
    #print_arr(arr)
print(result)