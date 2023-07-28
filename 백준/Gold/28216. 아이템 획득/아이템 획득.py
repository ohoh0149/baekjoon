import sys
input=sys.stdin.readline

n,q=map(int,input().split())
#box_lst=[]
move_lst=[]
#box_arr=[[0]*200001 for _ in range(200001)]
box_dic={}
for _ in range(n):
    x,y,w=map(int,input().split())
    box_dic[(x,y)]=w
    #box_lst.append((x,y,w))
for _ in range(q):
    d,v=map(int,input().split())
    move_lst.append((d,v))
#print(box_lst)
dx=[1,0,-1,0]
dy=[0,1,0,-1]
sx,sy=1,1
result=0
for d ,v in move_lst:
    for _ in range(1,v+1):
        sx=sx+dx[d]
        sy=sy+dy[d]
        if (sx, sy) in box_dic.keys():
            result += box_dic[(sx, sy)]
print(result)

