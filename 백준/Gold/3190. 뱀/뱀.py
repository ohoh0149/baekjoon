from collections import  deque

def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

n=int(input())
k=int(input())

arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    x,y=map(int,input().split())
    arr[x][y]=1

l=int(input())
lst=[]
for _ in range(l):
    x,d=input().split()
    if d=="L":
        d=-1
    elif d=="D":
        d=1
    lst.append((int(x),d))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
d=1
q=deque()
q.append((1,1))
arr[1][1]=2
result=0
for turn in range(1,10001):
    if len(lst)>0 and lst[0][0]==turn-1:
        d=(d+lst[0][1])%4
        del lst[0]
    #현재 머리의 좌표
    x,y=q[-1][0],q[-1][1]
    #다음 머리의 좌표
    nx=x+dx[d]
    ny=y+dy[d]
    q.append((nx,ny))
    if not in_range(nx,ny) or arr[nx][ny]==2:
        result=turn
        break
    #사과가 있는 경우
    if arr[nx][ny]==1:
        arr[nx][ny]=2
    #사과가 없는 경우
    else:
        arr[nx][ny]=2
        arr[q[0][0]][q[0][1]]=0
        q.popleft()

    # print(turn)
    # for i in range(1,n+1):
    #     print(*arr[i][1:])
    # print()

print(result)










