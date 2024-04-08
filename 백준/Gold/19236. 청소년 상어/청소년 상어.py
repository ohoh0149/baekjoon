import copy
arr=[]
for _ in range(4):
    temp_lst=list(map(int,input().split()))
    temp=[]
    for i in range(0,8,2):
        temp.append([temp_lst[i],temp_lst[i+1]-1])
    arr.append(temp)


a,b=arr[0][0]
arr[0][0][0]=-1

#num의 pos찾기
def find_num_pos(num,arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0]==num:
                return (i,j)

    return -1,-1

def in_range(x,y):
    return 0<=x<4 and 0<=y<4
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def move_fish(arr):
    for fish_num in range(1,17):
        x,y=find_num_pos(fish_num,arr)
        if x==-1:
            continue
        fish_d=arr[x][y][1]
        for d in range(8):
            cur_d=(fish_d+d)%8
            nx=x+dx[cur_d]
            ny=y+dy[cur_d]
            if in_range(nx,ny) and 0<=arr[nx][ny][0]<=16:
                #arr[nx][ny],arr[x][y]
                arr[x][y]=arr[nx][ny]
                arr[nx][ny]=[fish_num,cur_d]
                break



result=0
def dfs(cur_arr,cur_result):
    global result
    result=max(result,cur_result)


    move_fish(cur_arr)
    sx,sy=find_num_pos(-1,cur_arr)
    sd=cur_arr[sx][sy][1]
    tx,ty=sx,sy
    for _ in range(3):
        tx=tx+dx[sd]
        ty=ty+dy[sd]
        if not in_range(tx,ty):
            break
        #물고기 있으면 ㄱ
        if 1<=cur_arr[tx][ty][0]<=16:
            temp_arr=copy.deepcopy(cur_arr)
            temp_arr[sx][sy]=[0,0]
            tem=temp_arr[tx][ty][0]
            temp_arr[tx][ty][0]=-1
            dfs(temp_arr,cur_result+tem)



dfs(arr,a)
print(result)


