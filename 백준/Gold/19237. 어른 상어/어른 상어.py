n,m,k=map(int,input().split())
shark_list=[]
for i in range(n):
    shark_list.append(list(map(int,input().split())))
shark_direction=[None]+list(map(int,input().split()))
mov=[[None]]
for i in range(1,m+1):
    temp_list=[[None]]
    for j in range(1,5):
        temp_list.append(list(map(int,input().split())))
    mov.append(temp_list)
# print(shark_list)
# print(shark_direction)
# print(mov)

smell_graph=[[[0,0] for i in range(n)] for i in range(n)]

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

def move_shark():
    global shark_list
    global shark_direction
    new_shark_list=[[0]*n for _ in range(n)]
    new_shark_direction=[0]*(m+1)
    for i in range(n):
        for j in range(n):

            newi,newj=-1,-1
            temp_dir=0
            shark_num=shark_list[i][j]
            if shark_list[i][j]>0:
                #냄새없는 칸 찾기
                for d in range(4):
                    nx=i+dx[mov[shark_num][shark_direction[shark_num]][d]]
                    ny=j+dy[mov[shark_num][shark_direction[shark_num]][d]]
                    if 0<=nx<n and 0<=ny<n and smell_graph[nx][ny][0]==0:
                        temp_dir=mov[shark_num][shark_direction[shark_num]][d]
                        newi,newj=nx,ny
                        break
                #자신의 냄새에 해당하는 칸 찾기
                if newi==-1 and newj==-1:
                    for d in range(4):
                        nx = i + dx[mov[shark_num][shark_direction[shark_num]][d]]
                        ny = j + dy[mov[shark_num][shark_direction[shark_num]][d]]
                        if 0 <= nx < n and 0 <= ny < n and smell_graph[nx][ny][0] == shark_num:
                            newi, newj = nx, ny
                            temp_dir = mov[shark_num][shark_direction[shark_num]][d]
                            break
                if new_shark_list[newi][newj]==0 or new_shark_list[newi][newj]>shark_num:
                    new_shark_list[newi][newj]=shark_num
                    new_shark_direction[shark_num]=temp_dir

            #집어넣기



    shark_list=new_shark_list
    shark_direction=new_shark_direction

#시작 냄새 뿌리기
for i in range(n):
    for j in range(n):
        if shark_list[i][j]>0:
            smell_graph[i][j][0]=shark_list[i][j]
            smell_graph[i][j][1]=k

result=-1

for l in range(1,1001):
    move_shark()



    for i in range(n):
        for j in range(n):
            if smell_graph[i][j][1]>1:
                smell_graph[i][j][1]-=1
            elif smell_graph[i][j][1]==1:
                smell_graph[i][j][1]=0
                smell_graph[i][j][0]=0
    count=0
    for i in range(n):
        for j in range(n):
            if shark_list[i][j]>0:
                count+=1
                smell_graph[i][j][0],smell_graph[i][j][1]=shark_list[i][j],k
    if count==1:
        result=l
        break


print(result)