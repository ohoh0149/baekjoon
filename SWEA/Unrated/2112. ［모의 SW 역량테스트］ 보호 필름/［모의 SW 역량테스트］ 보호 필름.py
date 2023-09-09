import copy
from itertools import combinations
from itertools import product

def check_arr(arr):
    for j in range(w):
        max_count=1
        cur_count=1
        for i in range(1,d):
            if arr[i][j]==arr[i-1][j]:
                cur_count+=1
                max_count=max(max_count,cur_count)
            else:
                cur_count=1
        #print(max_count,end=" ")
        if max_count<k:
            return False

    return True

def dfs(k,count):
    global arr
    global result
    if count>=result:
        return
    if k==d:
        if check_arr(arr):
            result=min(result,count)
        return
    for i in [-1,0,1]:
        if i==-1:
            dfs(k+1,count)
        else:
            ori_lst=arr[k]
            arr[k]=[i]*w
            dfs(k+1,count+1)
            arr[k]=ori_lst






T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    d,w,k=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(d)]
    result=1e9
    dfs(0,0)

    print("#"+str(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
