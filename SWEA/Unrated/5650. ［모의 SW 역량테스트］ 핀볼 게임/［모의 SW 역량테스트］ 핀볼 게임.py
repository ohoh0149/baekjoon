
def in_range(x,y):
    return 0<=x<n and 0<=y<n
dx=[-1,0,1,0]
dy=[0,1,0,-1]
d_lst=[0,[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,0,3,1],[2,3,0,1]]


def get_result(sx,sy,sd):
    x,y=sx,sy
    d=sd
    count=0
    while True:
        nx=x+dx[d]
        ny=y+dy[d]
        if nx==sx and ny==sy:
            break
        if not in_range(nx,ny):
            count+=1
            d=(d+2)%4
        elif arr[nx][ny]==0:
            pass
        elif 1<=arr[nx][ny]<=5:
            d=d_lst[arr[nx][ny]][d]
            count+=1
        elif 6<=arr[nx][ny]<=10:
            nx,ny=w_dic[(nx,ny)]
        elif arr[nx][ny]==-1:
            break
        x,y=nx,ny

    return count


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    w_dic=dict()
    w_lst=[[] for _ in range(11)]
    for i in range(n):
        for j in range(n):
            if 6<=arr[i][j]<=10:
                w_lst[arr[i][j]].append((i,j))
    for i in range(6,11):
        if len(w_lst[i])>0:
            w_dic[w_lst[i][0]]=w_lst[i][1]
            w_dic[w_lst[i][1]]=w_lst[i][0]
    result=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                for d in range(4):
                    cur_result=get_result(i,j,d)
                    result=max(result,cur_result)

    print("#"+str(test_case),result)






    # ///////////////////////////////////////////////////////////////////////////////////
