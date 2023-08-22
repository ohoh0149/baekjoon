from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]



def turn_lst(i,d,k):
    global arr
    k=k%m
    s=0
    if d==0:
        s=(s-k+m)%m
    elif d==1:
        s+=k
    arr[i]=arr[i][s:]+arr[i][:s]


def turn(x,d,k):
    for i in range(x-1,n,x):
        turn_lst(i,d,k)

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def remove_num():
    global arr
    visited=[[0]*m for _ in range(n)]
    remove_flag=False
    for i in range(n):
        for j in range(m):
            if visited[i][j]!=0 or arr[i][j]==0:
                continue
            visited[i][j]=1
            q=deque()
            q.append((i,j))
            pos_lst=[(i,j)]
            while q:
                x,y=q.popleft()
                for d in range(4):
                    nx=x+dx[d]
                    ny=(y+dy[d]+m)%m
                    if in_range(nx,ny) and visited[nx][ny]==0 and arr[x][y]==arr[nx][ny]:
                        pos_lst.append((nx,ny))
                        q.append((nx,ny))
                        visited[nx][ny]=1
            if len(pos_lst)>=2:
                remove_flag=True
                for x,y in pos_lst:
                    arr[x][y]=0
    return remove_flag





def normalize():
    global  arr
    count=0
    sm=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                count+=1
                sm+=arr[i][j]
    if count==0:
        return True
    avg=sm/count
    #print("avg",avg)

    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 :
                if arr[i][j]>avg:
                    arr[i][j]-=1
                elif arr[i][j]<avg:
                    arr[i][j]+=1
    return False


n,m,t=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

#turn(2,0,0)
def print_arr(arr):
    for i in range(n):
        print(arr[i])
    print()

for _ in range(t):
    x,d,k=map(int,input().split())
    turn(x,d,k)
    #print_arr(arr)
    flag=remove_num()
    #print_arr(arr)
    if not flag:
        if normalize():
            break

result=0
for i in range(n):
    result+=sum(arr[i])
print(result)
