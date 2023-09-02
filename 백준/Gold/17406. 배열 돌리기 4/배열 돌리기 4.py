import copy
from  itertools import permutations
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def turn(arr,x1,y1,x2,y2):
    temp=arr[x1][y1]
    d=2
    x,y=x1,y1
    while True:

        nx=x+dx[d]
        ny=y+dy[d]
        if not( x1<=nx<=x2 and y1<=ny<=y2):
            d=(d+3)%4
            nx=x+dx[d]
            ny=y+dy[d]
        if nx==x1 and ny==y1:
            break
        arr[x][y]=arr[nx][ny]
        x,y=nx,ny
    arr[x][y]=temp

def get_result(arr):
    res=1e9
    for i in range(n):
        res=min(res,sum(arr[i]))
    return res


def turn_arr(arr,a):
    for v in a:
        r,c,s=turn_lst[v]
        for i in range(1,s+1):
            turn(arr,r-i,c-i,r+i,c+i)

n,m,k=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(n)]
turn_lst=[]
for _ in range(k):
    r,c,s=map(int,input().split())
    turn_lst.append((r-1,c-1,s))
l=len(turn_lst)

result=1e9
for a in permutations(range(l),l):
    new_arr=copy.deepcopy(arr)
    turn_arr(new_arr,a)
    val=get_result(new_arr)
    result=min(val,result)
print(result)