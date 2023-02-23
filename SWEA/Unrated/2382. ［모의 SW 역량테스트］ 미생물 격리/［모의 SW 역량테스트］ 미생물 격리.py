

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
        # ///////////////////////////////////////////////////////////////////////////////////
    n, m, k = map(int, input().split())
    graph = [[0] * n for i in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(k):
        r, c, num, d = map(int, input().split())
        graph[r][c]=[num,d-1,0]
    for _ in range(m):
        new_graph=[[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j]==0 or graph[i][j][0]==0:
                    continue
                else:
                    dir=graph[i][j][1]
                    nx=i+dx[dir]
                    ny=j+dy[dir]
                    if nx==n-1 or nx==0 or ny==n-1 or ny==0:
                        temp_dir=0
                        if dir==0:
                            temp_dir=1
                        elif dir==1:
                            temp_dir=0
                        elif dir==2:
                            temp_dir=3
                        elif dir==3:
                            temp_dir=2
                        new_graph[nx][ny]=[graph[i][j][0]//2,temp_dir,graph[i][j][0]//2]
                    else:
                        if new_graph[nx][ny]==0:
                            new_graph[nx][ny]=[graph[i][j][0],dir,graph[i][j][0]]
                        else:
                            new_graph[nx][ny][0] += graph[i][j][0]
                            if new_graph[nx][ny][2]<graph[i][j][0]:
                                new_graph[nx][ny][1]=dir
                                new_graph[nx][ny][2]=graph[i][j][0]
        graph=new_graph


    result=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]==0:
                continue
            else:
                result+=graph[i][j][0]
    print("#"+str(test_case),result)







    #print(graph)


    # ///////////////////////////////////////////////////////////////////////////////////
