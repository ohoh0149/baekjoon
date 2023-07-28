import copy
import sys
input=sys.stdin.readline

def find_idx(num,d):
    l=0
    r=len(box_lst[d])-1
    while l<=r:
        m=(l+r)//2
        if box_lst[d][m][d]<num:
            l=m+1
        elif box_lst[d][m][d]>num:
            r=m-1
        else:
            return m
    return -1

def find_left_idx(num,d):
    l=0
    r=len(box_lst[d])-1
    left_idx=-1
    while l<=r:
        m=(l+r)//2
        if box_lst[d][m][d]<num:
            l=m+1
        elif box_lst[d][m][d]>num:
            r=m-1
        else:
            left_idx=m
            r=m-1
    return left_idx

n,q=map(int,input().split())
box_lst=[]
move_lst=[]
for _ in range(n):
    x,y,w=map(int,input().split())
    box_lst.append((x,y,w))
box_lst.sort()
for _ in range(q):
    d,v=map(int,input().split())
    move_lst.append((d,v))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
sx,sy=1,1
result=0

y_box_lst=copy.deepcopy(box_lst)
y_box_lst.sort(key=lambda x:(x[1],x[0]))
box_lst=[box_lst,y_box_lst]




l=len(box_lst[0])
for d ,v in move_lst:

    nx=sx+v*dx[d]
    ny=sy+v*dy[d]
    spos=(sx,sy)
    pos=(nx,ny)
    flag=0


    if d%2==0:
        idx=find_left_idx(ny,1)
        flag=1
    else:
        idx=find_left_idx(nx,0)
        flag=0
    if idx==-1:

        sx,sy=nx,ny
        continue
    val=box_lst[flag][idx][flag]

    r_flag=(flag+1)%2


    for i in range(idx,l):
        mn=min(spos[r_flag],pos[r_flag])
        mx=max(spos[r_flag],pos[r_flag])
        if box_lst[flag][i][flag]!=val:
            break


        elif mn<=box_lst[flag][i][r_flag]<=mx and spos[r_flag]!=box_lst[flag][i][r_flag]:
            result+=box_lst[flag][i][2]

    sx,sy=nx,ny


print(result)

