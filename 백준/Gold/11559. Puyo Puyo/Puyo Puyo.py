from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<12 and 0<=y<6

def bomb_all():
    global arr
    flag=False
    visited=[[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j]=="." or visited[i][j]==1:
                continue
            color=arr[i][j]
            pos_lst=[(i,j)]
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if in_range(nx,ny) and visited[nx][ny]==0 and arr[nx][ny]==color:
                        pos_lst.append((nx,ny))
                        visited[nx][ny]=1
                        q.append((nx,ny))
            if len(pos_lst)>3:
                flag=True
                for x,y in pos_lst:
                    arr[x][y]="."

    return flag

def move_down():
    global arr
    new_arr=[["."]*6 for _ in range(12)]
    for j in range(6):
        idx=11
        for i in range(11,-1,-1):
            if arr[i][j]!=".":
                new_arr[idx][j]=arr[i][j]
                idx-=1
    arr=new_arr





arr=[]
for _ in range(12):
    inp=input()
    lst=[]
    for s in inp:
        lst.append(s)
    arr.append(lst)

count=0
while True:
    if not bomb_all():
        break
    move_down()
    count+=1
    # for i in range(12):
    #     print(arr[i])
print(count)