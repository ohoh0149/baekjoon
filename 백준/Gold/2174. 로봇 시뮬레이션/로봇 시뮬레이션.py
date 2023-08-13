a,b=map(int,input().split())
n,m=map(int,input().split())
robot_lst=[]
arr=[[0]*(b+1) for _ in range(a+1)]
#print(arr)

def in_range(x,y):
    return 1<=x<=a and 1<=y<=b
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in range(1,n+1):
    inp=input().split()
    if inp[2]=="N":
        d=0
    elif inp[2]=="E":
        d=1
    elif inp[2]=="S":
        d=2
    elif inp[2]=="W":
        d=3
    robot_lst.append([int(inp[0]),int(inp[1]),d])
    arr[int(inp[0])][int(inp[1])]=i


end_flag=False
for _ in range(m):
    query=input().split()
    num=int(query[0])-1
    turn=int(query[2])
    if query[1]=="L":
        turn=turn%4
        for _ in range(turn):
            robot_lst[num][2]=(robot_lst[num][2]+3)%4
    elif query[1]=="R":
        turn=turn%4
        for _ in range(turn):
            robot_lst[num][2]=(robot_lst[num][2]+1)%4
    elif query[1]=="F":
        d=robot_lst[num][2]
        for _ in range(turn):
            x,y=robot_lst[num][0],robot_lst[num][1]
            nx,ny=x+dx[d],y+dy[d]
            #print(x,y,nx,ny)
            if not in_range(nx,ny):
                print("Robot",num+1,"crashes into the wall")
                end_flag=True
                break
            if arr[nx][ny]!=0:
                print("Robot",num+1,"crashes into robot",arr[nx][ny])
                end_flag=True
                break
            arr[x][y]=0
            arr[nx][ny]=num+1
            robot_lst[num][0], robot_lst[num][1]=nx,ny
    if end_flag:
        break

#print(arr)
#print(robot_lst)
if not end_flag:
    print("OK")