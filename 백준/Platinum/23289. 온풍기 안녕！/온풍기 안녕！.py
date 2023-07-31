from collections import deque

def in_range(x,y):
    return 0<=x<r and 0<=y<c

def hot_one(hx,hy,hd):
    global hot_arr
    visited = [[0] * c for _ in range(r)]
    sx = hx + dx[hd]
    sy = hy + dy[hd]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 5
    while q:
        x, y = q.popleft()
        hot_arr[x][y] += visited[x][y]
        if visited[x][y]==0:
            break
        #일단 먼저 상 우 하로 이동하자!
        for d in range(-1, 2):
            nx = x + dx[(hd + d) % 4]
            ny = y + dy[(hd + d) % 4]
            #일단 시작 점에서 다음 위치로 벽 있다면
            if wall_arr[x][y][(hd+d)%4]==1:
                continue
            #d==-1 or d==1일때 추가로 벽있는지 확인
            if d==-1 or d==1:
                if in_range(nx,ny) and  wall_arr[nx][ny][hd]==1:
                    continue
                else:
                    nx+=dx[hd]
                    ny+=dy[hd]
            #벽이 없는거 확인 완료
            if in_range(nx,ny) and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]-1
                q.append((nx,ny))
    #print_arr(visited)


def step1():
    global hot_arr
    for hx,hy,hd in hitter_lst:
        hot_one(hx,hy,hd)


#온도가 조절됨
def step2():
    global hot_arr
    visited=[[0]*c for _ in range(r)]
    new_arr=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            visited[i][j]=1
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                #범위 안이고 벽이 없고 이미 비교했던 곳이 아니라면
                if in_range(nx,ny) and wall_arr[i][j][d]==0 and visited[nx][ny]==0:
                    cha=hot_arr[i][j]-hot_arr[nx][ny]
                    val=abs(cha)//4
                    if cha>0:
                        new_arr[i][j]-=val
                        new_arr[nx][ny]+=val
                    else:
                        new_arr[i][j]+=val
                        new_arr[nx][ny]-=val
    for i in range(r):
        for j in range(c):
            hot_arr[i][j]+=new_arr[i][j]



def step3():
    global hot_arr
    for i in range(r):
        for j in range(c):
            if i==0 or i==r-1 or j==0 or j==c-1 :
                if hot_arr[i][j]>0:
                    hot_arr[i][j]-=1




def check_end():
    for x,y in check_pos_lst:
        if hot_arr[x][y]<k:
            return False

    return True









def d_mapper(num):
    if num==1:
        return 1
    elif num==2:
        return 3
    elif num==3:
        return 0
    elif num==4:
        return 2

def print_arr(arr):
    for i in range(r):
        print(*arr[i])
    print()




r,c,k=map(int,input().split())

temp_arr=[]
for _ in range(r):
    temp_arr.append(list(map(int,input().split())))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
check_pos_lst=[]
hitter_lst=[]
hot_arr=[[0]*c for _ in range(r)]
wall_arr=[[[0,0,0,0] for _ in range(c)] for _ in range(r)]
w=int(input())
for _ in range(w):
    wx,wy,wt=map(int,input().split())
    wx-=1
    wy-=1
    wall_arr[wx][wy][wt]=1
    wnx=wx+dx[wt]
    wny=wy+dy[wt]
    if not in_range(wnx,wny):
        continue
    else:
        wall_arr[wnx][wny][(wt+2)%4]=1

for i in range(r):
    for j in range(c):
        if temp_arr[i][j]==0:
            continue
        elif temp_arr[i][j]==5:
            check_pos_lst.append((i,j))
        #온풍기
        else:
            hitter_lst.append((i,j,d_mapper(temp_arr[i][j])))

#print_arr(hot_arr)
#print(check_pos_lst)
#print(hitter_lst)
#print_arr(wall_arr)

result=101
for turn in range(1,101):
    step1()
  #  print_arr(hot_arr)
    step2()
 #   print_arr(hot_arr)
    step3()
    if check_end():
        result=turn
        break
#print_arr(hot_arr)
print(result)

