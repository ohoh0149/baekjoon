#import sys
#sys.stdin = open("input.txt", "r")

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def check(x,y,d):
    while True:
        x=x+dx[d]
        y=y+dy[d]
        if not in_range(x,y):
            return True
        if arr[x][y]!=0:
            return False


def put(x,y,d):
    global arr
    count=0
    while True:
        x=x+dx[d]
        y=y+dy[d]
        if not in_range(x,y):
            return count
        arr[x][y]=2
        count+=1
def rm(x,y,d):
    global arr
    while True:
        x = x + dx[d]
        y = y + dy[d]
        if not in_range(x, y):
            return
        arr[x][y] = 0


def dfs(k,count,length):
    global max_core_count
    global min_sum_length
    if k==l:
        if count>max_core_count:
            min_sum_length=length
            max_core_count=count
        elif count==max_core_count:
            min_sum_length=min(min_sum_length,length)
        return

    x,y=pos_lst[k]
    for d in range(4):
        if check(x,y,d):
            temp=put(x,y,d)
            dfs(k+1,count+1,length+temp)
            rm(x,y,d)

    dfs(k+1,count,length)











T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]

    max_core_count=0
    min_sum_length=1e9

    outer_count=0

    pos_lst=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                continue
            if i==0 or i==n-1 or j==0 or j==n-1:
                outer_count+=1
            else:
                pos_lst.append((i,j))
    l=len(pos_lst)
    dfs(0,outer_count,0)
    print("#"+str(test_case),min_sum_length)



    # ///////////////////////////////////////////////////////////////////////////////////
