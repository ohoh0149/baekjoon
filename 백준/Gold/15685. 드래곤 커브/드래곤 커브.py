def rotate_point(x,y,cx,cy):
    return cy-y+cx,x-cx+cy

dx=[1,0,-1,0]
dy=[0,-1,0,1]
def make_dragon_curve(x,y,d,g):
    cx,cy=x+dx[d],y+dy[d]
    pos_lst=[(x,y),(cx,cy)]
    for _ in range(g):
        for ax, ay in pos_lst[:]:
            pos_lst.append(rotate_point(ax,ay,cx,cy))
        cx,cy=rotate_point(x,y,cx,cy)
    pos_lst = list(set(pos_lst))
    return pos_lst
    #print(pos_lst)

def in_range(x,y):
    return 0<=x<=100 and 0<=y<=100



n=int(input())

#make_dragon_curve(0,0,0,3)
#exit()
arr=[[0]*101 for _ in range(101)]
for _ in range(n):
    x,y,d,g=map(int,input().split())
    pos_s=make_dragon_curve(x,y,d,g)
    #print(pos_s)
    for ax,ay in pos_s:
        if in_range(ax,ay):
            arr[ax][ay]=1


result=0
for i in range(100):
    for j in range(100):
        x,y=i,j
        flag=True
        for d in range(4):
            if arr[x][y]==0:
                flag=False
                break
            x,y=x+dx[(d+3)%4],y+dy[(d+3)%4]
        if flag:
            #print(i,j)
            result+=1


print(result)

