from itertools import combinations


def check_ok():
    for sx,sy in teacher_lst:
        for d in range(4):
            x,y=sx,sy
            for _ in range(n):
                x=x+dx[d]
                y=y+dy[d]
                if (not in_range(x,y)) or arr[x][y]=="O":
                    break
                if arr[x][y]=="S":
                    return False
    return True



dx=[-1,0,1,0]
dy=[0,1,0,-1]
def in_range(x,y):
    return 0<=x<n and 0<=y<n

n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().split())

teacher_lst=[]
pos_lst=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]=="T":
            teacher_lst.append((i,j))

        elif arr[i][j]=="X":
            pos_lst.append((i,j))


result_flag=False
case_lst=list(combinations(pos_lst,3))
for case in case_lst:
    for x,y in case:
        arr[x][y]="O"

    if check_ok():
        result_flag=True
        break

    for x,y in case:
        arr[x][y]="X"

if result_flag:
    print("YES")
else:
    print("NO")