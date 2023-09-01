import copy


def get_next_arr(arr):
    next_arr=[]
    for j in range(len(arr[0])):
        cur_lst=[]
        for i in range(len(arr)-1,-1,-1):
            cur_lst.append(arr[i][j])
        next_arr.append(cur_lst)
    cur_lst=[]
    for j in range(len(arr[0]),len(arr[-1])):
        cur_lst.append(arr[-1][j])
    if len(cur_lst)>0:
        next_arr.append(cur_lst)
    return next_arr


def step2(lst):
    arr=[lst]
    arr.insert(0,[arr[0].pop(0)])

    while True:
        next_arr=get_next_arr(arr)
        if len(next_arr[0])>len(next_arr[-1]) or len(arr[0])==len(arr[-1]):
            break
        arr=next_arr
    return arr

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def step3():
    global arr
    add_arr=[[0]*len(arr[-1]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j,num in enumerate(arr[i]):
            l=len(arr[i])
            for d in range(1,3):
                nx=i+dx[d]
                ny=j+dy[d]
                if 0<=nx<len(arr) and 0<=ny<len(arr[i]):
                    s=abs(arr[nx][ny]-arr[i][j])//5
                    if s>0:
                        if arr[nx][ny]>arr[i][j]:
                            add_arr[nx][ny]-=s
                            add_arr[i][j]+=s
                        else:
                            add_arr[nx][ny]+=s
                            add_arr[i][j]-=s

    for i,lst in enumerate(arr):
        for j,num in enumerate(lst):
            arr[i][j]+=add_arr[i][j]

def step4(arr):
    lst=[]
    for j in range(len(arr[0])):
        for i in range(len(arr)-1,-1,-1):
            lst.append(arr[i][j])

    for j in range(len(arr[0]),len(arr[-1])):
        lst.append(arr[-1][j])
    return lst


def step5(lst):
    arr=[lst[:n//2][::-1],lst[n//2:]]

    lst1=arr[0]
    lst2=arr[1]
    m=n//2
    new_arr=[lst2[:m//2][::-1],lst1[:m//2][::-1],lst1[m//2:],lst2[m//2:]]
    return new_arr






n,k=map(int,input().split())
lst=list(map(int,input().split()))

#step2([1,2,3,4,5,6,7,8])
#exit()

count=0
while True:
    if max(lst)-min(lst)<=k:
        break
    count+=1
    min_val=min(lst)
    #1 최솟값 찾아서 +1
    for idx,num in enumerate(lst):
        if num==min_val:
            lst[idx]+=1

    #2 어항 쌓기
    arr=step2(lst)

    #3 수 조절
    step3()
    lst=step4(arr)

    arr=step5(lst)

    step3()
    lst=step4(arr)


print(count)
