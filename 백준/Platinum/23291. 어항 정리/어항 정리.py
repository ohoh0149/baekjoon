n,k=map(int,input().split())
lst=list(map(int,input().split()))

result=0


def step2_turn(arr):
    c=len(arr[0])
    r=len(arr)
    new_arr=[]
    for j in range(c):
        temp_lst=[]
        for i in range(r-1,-1,-1):
            temp_lst.append(arr[i][j])
        new_arr.append(temp_lst)
    new_arr.append(arr[r-1][c:])
    return new_arr



def step2(lst):
    arr=[[lst[0]],lst[1:]]
    while True:
        next_arr=step2_turn(arr)
        if len(next_arr[0])>len(next_arr[-1]):
            break
        arr=next_arr
    return arr


dx=[-1,0,1,0]
dy=[0,1,0,-1]

def step3(arr):
    r=len(arr)
    c=len(arr[-1])
    def in_range(x,y):
        return 0<=x<r and 0<=y<c
    new_arr=[[0]*c for _ in range(r)]
    for i in range(r):
        for j,val in enumerate(arr[i]):
            new_arr[i][j]=val

    for i in range(r):
        for j in range(c):
            if new_arr[i][j]==0:
                continue
            for d in range(1,3):
                nx=i+dx[d]
                ny=j+dy[d]
                if not in_range(nx,ny) or new_arr[nx][ny]==0:
                    continue
                v=(abs(arr[i][j]-arr[nx][ny]))//5
                if v>0:
                    if arr[i][j]>arr[nx][ny]:
                        new_arr[i][j]-=v
                        new_arr[nx][ny]+=v
                    else:
                        new_arr[i][j]+=v
                        new_arr[nx][ny]-=v
    return new_arr


def step4(arr):
    r=len(arr)
    c=len(arr[-1])
    lst=[]
    for j in range(c):
        for i in range(r-1,-1,-1):
            if arr[i][j]!=0:
                lst.append(arr[i][j])
    return lst


def step5(lst):
    l=len(lst)//4
    arr=[list(reversed(lst[2*l:3*l])),lst[l:2*l],list(reversed(lst[0:l])),lst[3*l:]]
    return arr

while True:
    #종료 조건
    if max(lst)-min(lst)<=k:
        break
    result+=1
    #1
    mi=min(lst)
    for idx,val in enumerate(lst):
        if val==mi:
            lst[idx]+=1
    #2
    arr=step2(lst)

    #3
    arr=step3(arr)
    #4
    lst=step4(arr)
    #5
    arr=step5(lst)

    arr=step3(arr)

    lst=step4(arr)

print(result)

