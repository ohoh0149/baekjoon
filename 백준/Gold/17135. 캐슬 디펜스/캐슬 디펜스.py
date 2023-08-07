import copy


def get_e_lst(arr,lst):
    e_lst = []
    for y in lst:
        # 죽일 적의 좌표
        ex, ey = -1, -1
        # 현재 까지의 최단 거리
        el = 1e9
        for i in range(n - 1, -1, -1):
            for j in range(m):
                l=abs(n-i)+abs(y-j)
                if arr[i][j] == 1 and l<=d:
                    if (l==el and j<ey) or l<el:
                        ex, ey = i, j
                        el = l
        e_lst.append((ex, ey))

    return e_lst

def move_down(arr):
    global total_count

    for i in range(n-1,-1,-1):
        for j in range(m):
            if arr[i][j]==0:
                continue
            if i==n-1:
                total_count-=1
                arr[i][j]=0
            else:
                arr[i][j]=0
                arr[i+1][j]=1



def get_result(arr,lst):

    global total_count
    catch_count=0
    while True:
        if total_count==0:
            break
        #죽일 적들 좌표 구하기
        e_lst=get_e_lst(arr,lst)
        #죽일 적들 좌표 제거(중복이어도 ㄱㅊ)
        for x,y in e_lst:
            if x==-1:
                continue
            if arr[x][y]==1:
                total_count-=1
                catch_count+=1
                arr[x][y]=0
        move_down(arr)


    return catch_count



def print_arr(arr):
    for i in range(n):
        print(*arr[i])




n,m,d=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

total_count=0
for lst in arr:
    for a in lst:
        if a==1:
            total_count+=1
tc=total_count
result=0
for x1 in range(m):
    for x2 in range(x1+1,m):
        for x3 in range(x2+1,m):
            #print(x1,x2,x3)
            new_arr=copy.deepcopy(arr)
            total_count=tc
            result=max(result,get_result(new_arr,[x1,x2,x3]))
            #print(result)
print(result)

