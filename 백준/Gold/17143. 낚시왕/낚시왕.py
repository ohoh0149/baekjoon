import copy


def in_range(x,y):
    return 0<=x<r and 0<=y<c
dx=[0,-1,1,0,0]
dy=[0,0,0,1,-1]



def get_end_pos_sub(x,y,d):
    if d==1:
        return 0,y,x
    elif d==2:
        return r-1,y,r-1-x
    elif d==3:
        return x,c-1,c-1-y
    elif d==4:
        return x,0,y

rd=[0,2,1,4,3]
#좌표랑 방향 반환
def get_next_pos(x,y,s,d):
    if d==1 or d==2:
        s=s%(2*(r-1))
    else:
        s=s%(2*(c-1))
    #print(s)
    nx=x+s*dx[d]
    ny=y+s*dy[d]
    if in_range(nx,ny):
        return nx,ny,d
    x,y,sub=get_end_pos_sub(x,y,d)
    s-=sub
    d=rd[d]

    nx = x + s * dx[d]
    ny = y + s * dy[d]
    if in_range(nx, ny):
        return nx,ny ,d

    x, y, sub = get_end_pos_sub(x, y, d)
    s -= sub
    d = rd[d]

    nx = x + s * dx[d]
    ny = y + s * dy[d]
    if in_range(nx, ny):
        return nx,ny,d

    print("this is error")
    return -1,-1,-1



def move_all_shark():
    global arr
    new_arr=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                ni,nj,nd=get_next_pos(i,j,arr[i][j][0],arr[i][j][1])
                if new_arr[ni][nj]==0:
                    new_arr[ni][nj]=[arr[i][j][0],nd,arr[i][j][2]]
                else:
                    if new_arr[ni][nj][2]<arr[i][j][2]:
                        new_arr[ni][nj]=[arr[i][j][0],nd,arr[i][j][2]]
    arr=new_arr













r,c,m=map(int,input().split())
arr=[[0]*c for _ in range(r)]
for _ in range(m):
    tr,tc,s,d,z=map(int,input().split())
    arr[tr-1][tc-1]=[s,d,z]
# for i in range(r):
#     print(arr[i])
#
# print(get_next_pos(0,2,5,2))
#
# print(get_next_pos(1,3,8,4))
#
# print(get_next_pos(3,0,3,3))
#
# print(get_next_pos(3,4,0,1))

result=0
for j in range(c):
    for i in range(r):
        if arr[i][j]!=0:
            result+=arr[i][j][2]
            #print(result)
            arr[i][j]=0
            break
    move_all_shark()
print(result)



