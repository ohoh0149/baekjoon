from itertools import combinations

def get_count(a,b):
    count=0
    w_count=0
    for i in range(a+1):
        w_count+=color_lst[i][0]

    b_count=0
    for i in range(a+1,b):
        b_count+=color_lst[i][1]
    r_count=0
    for i in range(b,n):
        r_count+=color_lst[i][2]

    count=n*m-w_count-b_count-r_count
    return count


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m=map(int,input().split())
    arr=[input() for _ in range(n)]
    color_lst=[]
    for i in range(n):
        w,b,r=0,0,0
        for j in range(m):
            if arr[i][j]=="W":
                w+=1
            elif arr[i][j]=="B":
                b+=1
            else:
                r+=1
        color_lst.append((w,b,r))
    result=1e9
    for a,b in combinations(range(n),2):
        if abs(b-a)==1:
            continue
        result=min(result,get_count(a,b))
    print("#"+str(test_case),result)



    # ///////////////////////////////////////////////////////////////////////////////////
