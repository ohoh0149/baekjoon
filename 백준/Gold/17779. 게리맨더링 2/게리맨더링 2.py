def in_range(lst):
    for x,y in lst:
        if  0<=x<n and 0<=y<n:
            pass
        else:
            return False
    return True


def get_result(ux,uy,lx,ly,dx,dy,rx,ry):
    sm_lst=[0]*5
    for x in range(n):
        for y in range(n):
            if x+y<ux+uy and y<=uy and x<lx:
                sm_lst[0]+=arr[x][y]
            elif x-y<ux-uy and y>uy and x<=rx:
                sm_lst[1]+=arr[x][y]
            elif x-y>lx-ly and x>=lx and y<dy:
                sm_lst[2]+=arr[x][y]
            elif x+y>dx+dy and x>=rx and y>=dy:
                sm_lst[3]+=arr[x][y]
            else:
                sm_lst[4]+=arr[x][y]

    return max(sm_lst)-min(sm_lst)




dr=[1,1,-1,-1]
dc=[-1,1,1,-1]

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]


result=1e9
for ux in range(n):
    for uy in range(n):
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                lx, ly = ux + d1 * dr[0], uy + d1 * dc[0]
                dx, dy = lx + d2 * dr[1], ly + d2 * dc[1]
                rx, ry = dx + d1 * dr[2], dy + d1 * dc[2]
                pos_lst=[(ux,uy),(lx,ly),(dx,dy),(rx,ry)]
                if in_range(pos_lst):
                    result=min(result,get_result(ux,uy,lx,ly,dx,dy,rx,ry))


print(result)