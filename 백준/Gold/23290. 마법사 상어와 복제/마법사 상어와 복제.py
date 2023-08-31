import copy
def in_range(x,y):
    return 1<=x<=4 and 1<=y<=4

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

def move_fish():
    global arr
    new_arr=[[[0,0,0,0,0,0,0,0] for _ in range(5)] for _ in range(5)]
    for i in range(1,5):
        for j in range(1,5):
            for l in range(8):
                if arr[i][j][l]==0:
                    continue
                x,y=i,j
                d=l
                find=False
                for _ in range(8):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and (not (sx==nx and sy==ny)) and smell_arr[nx][ny]<=0:
                        new_arr[nx][ny][d]+=arr[x][y][l]
                        find=True
                        break
                    d=(d+7)%8
                if not find:
                    new_arr[x][y][l]+=arr[x][y][l]
    arr=new_arr

def move_shark():
    global arr
    global smell_arr
    global sx,sy
    d_lst=[2,0,6,4]
    max_count=-1
    pos_lst=[]
    for d1 in d_lst:
        nx1=sx+dx[d1]
        ny1=sy+dy[d1]
        if not in_range(nx1,ny1):
            continue
        for d2 in d_lst:
            nx2 = nx1 + dx[d2]
            ny2 = ny1 + dy[d2]
            if not in_range(nx2, ny2):
                continue
            for d3 in d_lst:
                nx3 = nx2 + dx[d3]
                ny3 = ny2 + dy[d3]
                if not in_range(nx3, ny3):
                    continue
                #nx1 nx2 nx3

                lst=list(set([(nx1,ny1),(nx2,ny2),(nx3,ny3)]))
                count=0
                for x,y in lst:
                    count+=sum(arr[x][y])
                if count>max_count:
                    max_count=count
                    pos_lst=[(nx1,ny1),(nx2,ny2),(nx3,ny3)]


    sx,sy=pos_lst[2]

    for x,y in pos_lst:
        if sum(arr[x][y])!=0:
            arr[x][y]=[0,0,0,0,0,0,0,0]
            smell_arr[x][y]=3

def down_smell():
    global smell_arr
    for i in range(1,5):
        for j in range(1,5):
            if smell_arr[i][j]>=1:
                smell_arr[i][j]-=1

def print_arr(arr):
    for i in range(1,5):
        print(arr[i][1:])
    print()

m,s=map(int,input().split())

smell_arr=[[0]*5 for _ in range(5)]

arr=[[[0,0,0,0,0,0,0,0] for _ in range(5)] for _ in range(5)]
for _ in range(m):
    fx,fy,fd=map(int,input().split())
    arr[fx][fy][fd-1]+=1
sx,sy=map(int,input().split())




for _ in range(s):



    copy_arr=copy.deepcopy(arr)
    move_fish()



    move_shark()


    down_smell()

    for i in range(1,5):
        for j in range(1,5):
            for l in range(8):
                arr[i][j][l]+=copy_arr[i][j][l]







result=0
for i in range(1,5):
    for j in range(1,5):
        result+=sum(arr[i][j])
print(result)