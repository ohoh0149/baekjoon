n=int(input())
inp=input()
arr=[["#"]*101 for _ in range(101)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
d=2
x,y=50,50
min_x,min_y=50,50
max_x,max_y=50,50
arr[x][y]="."
for s in inp:
    if s=="R":
        d=(d+1)%4
        continue
    elif s=="L":
        d=(d+3)%4
        continue
    else:
        x=x+dx[d]
        y=y+dy[d]
        arr[x][y]="."

        min_x=min(min_x,x)
        min_y=min(min_y,y)
        max_x=max(max_x,x)
        max_y=max(max_y,y)


for i in range(min_x,max_x+1):
    for j in range(min_y,max_y+1):
        print(arr[i][j],end="")
    print()



