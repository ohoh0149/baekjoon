import copy


def turn(x,d,k):
    if d==0:
        a=1
    elif d==1:
        a=-1
    global arr
    for i in range(1,n+1):
        nx=i*x
        if nx>n:
            break
        #nx<=n-1
        before_list=arr[nx]
        after_list=[0]*m
        for j in range(m):
            after_list[(j+a*k+m)%m]=before_list[j]
        arr[nx]=after_list



dx=[0,-1,0,1]
dy=[1,0,-1,0]
#삭제하면 트루 삭제안하면 false반환
def remove_num():
    global arr
    new_arr=copy.deepcopy(arr)
    remove_flag=0
    for i in range(1,n+1):
        for j in range(m):
            if arr[i][j]==0:
                continue
            for d in range(4):
                nx=i+dx[d]
                ny=(j+dy[d])%m
                if arr[i][j]==arr[nx][ny]:
                    new_arr[i][j]=0
                    remove_flag=1
    arr=new_arr
    if remove_flag==1:
        return True
    else:
        return False


def normalization():
    sm=0
    for i in range(1,n+1):
        sm+=sum(arr[i])
    count=0
    for i in range(1,n+1):
        for j in range(m):
            if arr[i][j]!=0:
                count+=1
    if count==0:
        return
    md=sm/count
    for i in range(1,n+1):
        for j in range(m):
            if arr[i][j]==0:
                continue
            if arr[i][j]>md:
                arr[i][j]-=1
            elif arr[i][j]<md:
                arr[i][j]+=1

def get_result():
    global result
    for i in range(1,n+1):
        for j in range(m):
            result+=arr[i][j]




n,m,q=map(int,input().split())
arr=[[0]*m]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.append([0]*m)
#print(arr)
turn_info=[tuple(map(int,input().split())) for _ in range(q)]

result=0
for a,b,c in turn_info:
    turn(a,b,c)
    #print(arr)
    flag=remove_num()
    if not flag:
        normalization()

    #print(arr)
get_result()
print(result)