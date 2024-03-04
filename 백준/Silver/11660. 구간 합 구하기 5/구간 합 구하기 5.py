import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
sm_arr=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j==0:
            sm_arr[i][j]=arr[i][j]
        else:
            sm_arr[i][j]=arr[i][j]+sm_arr[i][j-1]

sm_arr2=[[0]*n for _ in range(n)]
for j in range(n):
    for i in range(n):
        if i==0:
            sm_arr2[i][j]=sm_arr[i][j]
        else:
            sm_arr2[i][j]=sm_arr2[i-1][j]++sm_arr[i][j]

sm_arr2.insert(0,[0]*(n+1))
for ls in sm_arr2:
    ls.insert(0,0)
for _ in range(m):
    result=0
    x1,y1,x2,y2=map(int,input().split())
    result+=sm_arr2[x2][y2]
    #print(result)
    result+=sm_arr2[x1-1][y1-1]
    #print(result)
    result-=sm_arr2[x2][y1-1]
    #print(result)
    result-=sm_arr2[x1-1][y2]
    print(result)

