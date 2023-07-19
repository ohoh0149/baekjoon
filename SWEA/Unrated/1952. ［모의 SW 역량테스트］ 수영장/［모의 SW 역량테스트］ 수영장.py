
#import sys
#sys.stdin = open("input.txt", "r")

def dfs(k,sm):
    global result
    if sm>=result:
        return 
    if k>=12:
        result=min(result,sm)
        return
    dfs(k+1,sm+lst[k]*d)
    dfs(k+1,sm+m)
    dfs(k+3,sm+m3)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    d,m,m3,y=map(int,input().split())
    result=y
    lst=list(map(int,input().split()))
    dfs(0,0)
    print("#"+str(test_case),result)
    # ///////////////////////////////////////////////////////////////////////////////////
