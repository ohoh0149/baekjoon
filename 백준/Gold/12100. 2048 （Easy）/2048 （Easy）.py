#한 리스트에 대해서 왼쪽으로 이동시키는 함수
import copy


def func(lst):
    #먼저 리스트에서 0을 제외한 숫자만 가지고 새로운 리스트를 만든다
    new_lst=[]
    for num in lst:
        if num!=0:
            new_lst.append(num)
    l=len(new_lst)
    if l==0:
        return lst
    #print(new_lst)
    #숫자가 합쳐질지 확인되었는지를 체크
    visited=[0]*l
    #합쳐진 숫자들을 저장하는 리스트 뒤에 0을 채워넣어야함.
    merge_lst=[]
    for i in range(l-1):
        if visited[i]==1:
            continue
        if visited[i]==0 and visited[i+1]==0 and new_lst[i]==new_lst[i+1]:
            #합체 된거 체크하고
            visited[i]=1
            visited[i+1]=1
            merge_lst.append(new_lst[i]*2)
        else:
            merge_lst.append(new_lst[i])
    if visited[l-1]==0:
        merge_lst.append(new_lst[l-1])


    #최종적으로 result_lst앞에서부터 채워넣기
    result_lst=[0]*n
    for idx,num in enumerate(merge_lst):
        result_lst[idx]=num
    return result_lst

#n=14
# 2 2 2 8 16 8 8 8 8
#print(func([0,0,2,2,0,2,8,0,16,8,0,8,8,8]))
def move_left(arr):
    for i in range(n):
        arr[i]=func(arr[i])
        #print(arr[i])
    return arr

def rotate90(arr):
    new_arr=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[j][n-1-i]=arr[i][j]
    return new_arr

def move(arr,d):
    #왼쪽인경우
    if d==0:
        arr=move_left(arr)
    else:
        for i in range(1,5):
            arr=rotate90(arr)
            #print(i,arr)
            if i==d:
                arr=move_left(arr)
             #   print("move after",i,arr)
    return arr



def get_max(arr):
    result=0
    for i in range(n):
        for j in range(n):
                result=max(arr[i][j],result)
    return result
def dfs(k,arr):
    global ans
    if k==5:
        ans=max(ans,get_max(arr))
        return
    for d in range(4):
        new_arr=copy.deepcopy(arr)
        new_arr=move(new_arr,d)
        dfs(k+1,new_arr)





n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

ans=0

#print(func([8,4,2]))
#print(move_left(arr))
#print(move(arr,3))
# arr=rotate90(arr)
# print(arr)
# arr=rotate90(arr)
# print(arr)
#print(get_max(arr))
dfs(0,arr)
print(ans)