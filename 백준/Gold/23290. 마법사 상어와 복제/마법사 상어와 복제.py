import copy

m,s=map(int,input().split())
arr=[[[0]*8 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x,y,d=map(int,input().split())
    arr[x-1][y-1][d-1]+=1
sx,sy=map(int,input().split())
sx-=1
sy-=1

smell_arr=[[0]*4 for _ in range(4)]


f_dx=[0,-1,-1,-1,0,1,1,1]
f_dy=[-1,-1,0,1,1,1,0,-1]
s_dx=[-1,0,1,0]
s_dy=[0,-1,0,1]

def in_range(x,y):
    return 0<=x<4 and 0<=y<4
def move_fish(arr):
    new_arr=[[[0]*8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for sd in range(8):
                if arr[i][j][sd]==0:
                    continue
                flag=False
                for t in range(8):
                    d=(sd-t+8)%8
                    nx=i+f_dx[d]
                    ny=j+f_dy[d]
                    if in_range(nx,ny) and (nx,ny)!=(sx,sy) and smell_arr[nx][ny]==0:
                        new_arr[nx][ny][d]+=arr[i][j][sd]
                        flag=True
                        break
                if not flag:
                    new_arr[i][j][sd]+=arr[i][j][sd]

    return new_arr


for _ in range(s):
    #1
    copy_arr=copy.deepcopy(arr)

    #2
    arr=move_fish(arr)

    #3
    result_d_lst=[]
    max_count=-1
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                d_lst=[d1,d2,d3]
                cur_count=0
                out_flag=False
                cx,cy=sx,sy
                visit_set=set()
                for d in d_lst:
                    cx=cx+s_dx[d]
                    cy=cy+s_dy[d]
                    if not in_range(cx,cy):
                        out_flag=True
                        break
                    if (cx,cy) not in visit_set:
                        cur_count+=sum(arr[cx][cy])
                        visit_set.add((cx,cy))
                if not out_flag:
                    if max_count<cur_count:
                        max_count=cur_count
                        result_d_lst=[d1,d2,d3]

    for d in result_d_lst:
        sx=sx+s_dx[d]
        sy=sy+s_dy[d]
        if sum(arr[sx][sy])>0:
            smell_arr[sx][sy]=3
            for t in range(8):
                arr[sx][sy][t]=0
    #4
    for i in range(4):
        for j in range(4):
            if smell_arr[i][j]>0:
                smell_arr[i][j]-=1

    for i in range(4):
        for j in range(4):
            for d in range(8):
                arr[i][j][d]+=copy_arr[i][j][d]


result=0
for i in range(4):
    for j in range(4):
        result+=sum(arr[i][j])
print(result)
