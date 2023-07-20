import copy
from collections import deque


def rotate_90():
    global arr
    n=len(arr)
    m=len(arr[0])
    new_arr=[[None]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_arr[j][n-1-i]=arr[i][j]
    arr=new_arr

def move_a(d):
    global arr
    if d==0:
        move_up()
    elif d==1:
        move_left()
    elif d==2:
        move_down()
    elif d==3:
        move_right()



def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def move(d):
    global arr
    global finish
    global fail
    n=len(arr)
    m=len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j]=="R":
                rx,ry=i,j
            if arr[i][j]=="B":
                bx,by=i,j
    if (rx!=bx and ry!=by) or (rx==bx and d%2==0) or (ry==by and d%2==1):
        arr[rx][ry]="."
        arr[bx][by]="."

        #nrx=rx+dx[d]
        #nry=ry+dy[d]
        while True:
            nrx = rx + dx[d]
            nry = ry + dy[d]
            if arr[nrx][nry]=="#":
                break
            if arr[nrx][nry]=="O":
                finish=1
                break
            rx=nrx
            ry=nry
        while True:
            nbx = bx + dx[d]
            nby = by + dy[d]
            if arr[nbx][nby] == "#":
                break
            if arr[nbx][nby] == "O":
                fail=1
                break
            bx = nbx
            by = nby
        arr[rx][ry]="R"
        arr[bx][by]="B"
    #행이 같은 경우
    else:
        move_a(d)



#파란색 사탕이 나오면 false반환 나머지는 true
def move_right():
    global finish
    global fail
    global arr
    n=len(arr)
    m=len(arr[0])
    for i in range(n): #한 행에 대해서
        start=0
        end=0
        while start<m-1:
            if arr[i][start]=="#" or arr[i][start]=="O":
                start+=1
                continue
            for j in range(start,m):
                if arr[i][j]!="#" and arr[i][j]!="O":
                    continue
                if arr[i][j]=="#":
                    r_lst=func(arr[i][start:j])
                    arr[i][start:j]=r_lst
                    start=j+1
                elif arr[i][j]=="O":
                    if "B" in arr[i][start:j]:
                        fail=1
                        return
                    elif "R" in arr[i][start:j]:
                        finish=1
                        return
                    else:
                        start=j+1


def move_left():
    rotate_90()
    rotate_90()
    move_right()
    rotate_90()
    rotate_90()


def move_up():
    rotate_90()
    move_right()
    rotate_90()
    rotate_90()
    rotate_90()

def move_down():
    rotate_90()
    rotate_90()
    rotate_90()
    move_right()
    rotate_90()





def func(lst):
    l=len(lst)
    br_lst=[]
    r_lst=["."]*l
    for i in lst:
        if i=="B"or i=="R":
            br_lst.append(i)
    #br_lst=[B,R,B,B,R,B,R]
    for i in range(l-1,-1,-1):
        if len(br_lst)==0:
            break
        a=br_lst.pop()
        r_lst[i]=a
    return r_lst

def print_arr(arr):
    n=len(arr)
    for i in range(n):
        print(arr[i])
    print()


def dfs(k,bd):
    #print(k)
    global move_count

    global arr
    n = len(arr)
    m = len(arr[0])
    global result
    global fail
    global finish
    if result!=-1 and k>result:
        return
    if fail:
        fail=0
        return
    if finish:
        finish=0
        if result==-1:
            result=k
        else:
            result=min(result,k)
        # if result==1:
        #     print_arr(arr)
        return
    if k==10:
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j]=="B":
                bx,by=i,j
            elif arr[i][j]=="R":
                rx,ry=i,j
    for d in range(3,-1,-1):
        if bd==d:
            continue
        finish=0
        fail=0
        move(d)
        dfs(k+1,d)
        for i in range(n):
            for j in range(m):
                if arr[i][j]=="B" or arr[i][j]=="R":
                    arr[i][j]="."
        arr[rx][ry]="R"
        arr[bx][by]="B"










# arr=['B','R','.','#']
# arr.sort()
# print(arr)
# exit()

move_count=0
n,m=map(int,input().split())
arr=[[None]*m for _ in range(n)]
for i in range(n):
    s=input()
    for j in range(m):
        arr[i][j]=s[j]
rx,ry=0,0
for i in range(n):
    for j in range(m):
        if arr[i][j]=="R":
            rx,ry=i,j
finish=0
fail=0
result=-1

visited=[[0]*m for _ in range(n)]
q=deque()
q.append((rx,ry))
visited[rx][ry]=1
find_flag=0
while q:
    x,y=q.popleft()
    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]!="#":
            if arr[nx][ny]=="O":
                find_flag=1
            q.append((nx,ny))
            visited[nx][ny]=1

if find_flag==1:
    dfs(0,-1)
# move(3)
# print(finish)
# print_arr(arr)
#
# move(2)
# print(finish)
# print_arr(arr)
# arr2=copy.deepcopy(arr)
# move(0)
# print_arr(arr)
# arr=arr2
#
# move_a(0)
# print_arr(arr)
print(result)
# arr=move_up(arr)
# print_arr(arr)
# arr=move_down(arr)
# print_arr(arr)
# arr=move_right(arr)
# print_arr(arr)
# arr=move_left(arr)
# print_arr(arr)
