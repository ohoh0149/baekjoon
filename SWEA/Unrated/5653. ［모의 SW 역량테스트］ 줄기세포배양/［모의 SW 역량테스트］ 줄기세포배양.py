dx=[-1,0,1,0]
dy=[0,1,0,-1]

def print_arr(arr):
    for i in range(-k,n+k):
        for j in range(-k,m+k):
            print(arr[i][j],end=" ")
        print()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m,k=map(int,input().split())
    arr=[[0]*(m+(k+1)) for _ in range(n+(k+1))]
    start_arr=[list(map(int,input().split())) for _ in range(n)]
    #print(start_arr)
    live_lst=[]
    for i in range(n):
        for j in range(m):
            # 생명력 , 상태 , 흐른 시간
            if start_arr[i][j]==0:
                continue
            arr[i][j]=[start_arr[i][j],0,0]
            live_lst.append((i,j))

    #초기 세팅 완료

    scope=k//2
    for _ in range(k):
        #new_arr=copy.deepcopy(arr)
        new_live_lst=[]
        #print(live_lst)
        #print(len(live_lst))
        for i ,j in live_lst:
            if arr[i][j][1]==-1:
                arr[i][j][1]=0
        for i,j in live_lst:
            #빈공간continue
            # if arr[i][j]==0:
            #     continue
            #죽은 상태면 continue
            # elif arr[i][j][1]==2:
            #     continue
            #비활성 상태 라면
            if arr[i][j][1]==0:
                new_live_lst.append((i,j))
                arr[i][j][1]=0
                arr[i][j][2]+=1
                #생명력과 흐른시간이 같다면
                if arr[i][j][0]==arr[i][j][2]:
                    #활성상태로 바꾸 흐른시간 초기화
                    arr[i][j][1]=1
                    arr[i][j][2]=0
            #활성 상태라면
            elif arr[i][j][1]==1:
                #첫 1시간동안만 번식
                if arr[i][j][2]==0:
                    for d in range(4):
                        nx=i+dx[d]
                        ny=j+dy[d]
                        #arr빈칸이고 현재 newarr nx ny 빈칸이거나 newarr에 있는애보다 생명력 클때 번식 가능
                        #print(new_arr[nx][ny],arr[i][j])
                        if arr[nx][ny]==0 or ( arr[nx][ny][1]==-1 and arr[nx][ny][0]<arr[i][j][0]):
                            if arr[nx][ny] == 0:
                                new_live_lst.append((nx, ny))
                            arr[nx][ny]=[arr[i][j][0],-1,0]
                #번식 완료후
                arr[i][j][2]+=1
                if arr[i][j][0]==arr[i][j][2]:
                    arr[i][j][1]=2
                    arr[i][j][2]=0
                else:
                    new_live_lst.append((i,j))
            else:
                print("this is error")
                print(arr[i][j])

        live_lst=new_live_lst
        #print("arr:")
        #print_arr(arr)
        #print(live_lst)
        #print(len(live_lst))

    result=len(live_lst)
    #print_arr(arr)
    # for i in range(-scope,n+scope+1):
    #     for j in range(-scope,m+scope+1):
    #         if arr[i][j]!=0 and arr[i][j][1]!=2:
    #             result+=1
    print("#"+str(test_case),result)



    # ///////////////////////////////////////////////////////////////////////////////////
