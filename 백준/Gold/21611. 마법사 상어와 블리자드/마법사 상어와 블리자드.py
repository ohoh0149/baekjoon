n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]
ball_lst=[]
#달팽이 배열 만들기
def make_snail_arr():
    global ball_lst
    snail_arr=[[0]*n for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x,y=0,0
    d=0
    for num in range(n*n-1,-1,-1):
        if arr[x][y]!=0:
            ball_lst.append(arr[x][y])
        snail_arr[x][y]=num
        nx=x+dx[d]
        ny=y+dy[d]
        if not in_range(nx,ny) or snail_arr[nx][ny]!=0:
            d=(d+1)%4
            nx=x+dx[d]
            ny=y+dy[d]
        x,y=nx,ny
    return snail_arr


def make_count_num(lst):
    lst.append(-1)
    result_lst=[]
    bef_num=0
    count=0
    for num in lst[1:]:
        if num==bef_num:
            count+=1
        else:
            if count!=0:
                result_lst.append((count,bef_num))
            count=1
        bef_num=num
    return result_lst





snail_arr=make_snail_arr()
ball_lst.append(0)
ball_lst=list(reversed(ball_lst))
result=[0,0,0,0]
for _ in range(m):
    di,si=map(int,input().split())
    rm_lst=[]
    cx,cy=n//2,n//2
    for _ in range(si):
        cx=cx+dx[di]
        cy=cy+dy[di]
        rm_lst.append(snail_arr[cx][cy])
    rm_lst.reverse()
    for temp in rm_lst:
        if len(ball_lst)>temp:
            del ball_lst[temp]

    #2 구슬 폭발
    while True:
        bomb_flag=False
        count_num_lst=make_count_num(ball_lst)
        new_ball_lst=[0]
        for count,num in count_num_lst:
            if count>=4:
                bomb_flag=True
                result[num]+=count
            else:
                new_ball_lst+=([num]*count)
        ball_lst=new_ball_lst
        if not  bomb_flag:
            break

    count_num_lst=make_count_num(ball_lst)
    ball_lst=[0]
    for count,num in count_num_lst:
        ball_lst.append(count)
        ball_lst.append(num)
    ball_lst=ball_lst[:n*n]

answer=0
for i in range(1,4):
    answer+=i*result[i]
print(answer)

