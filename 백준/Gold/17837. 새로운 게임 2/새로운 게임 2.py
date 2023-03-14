n,k=map(int,input().split())
color_board=[[0]*(n+1)]
for i in range(n):
    color_board.append([0]+list(map(int,input().split())))
token_list=[[0,0,0]]
for i in range(k):
    token_list.append(list(map(int,input().split())))
#print(color_board)
#print(token_list)
token_board=[[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        token_board[i][j]=[]
for num in range(1,k+1):
    token_board[token_list[num][0]][token_list[num][1]].append(num)
#print(token_board)



dx=[0,0,0,-1,1]
dy=[0,1,-1,0,0]

reverse=[0,2,1,4,3]

endflag=0
result=-1
for turn in range(1,1001):
    num=1
    flag=0
    while num<=k:
        # if flag==0:
        dir=token_list[num][2]
        # elif flag==1:
        #     dir=reverse[token_list[num][2]]
        x,y=token_list[num][0],token_list[num][1]
        nx,ny=x+dx[dir],y+dy[dir]
        if (nx<1 or nx>n or ny<1 or ny>n) or color_board[nx][ny]==2:
            if flag==0:
                flag=1
                token_list[num][2]=reverse[token_list[num][2]]
                continue
            elif flag==1:
                flag=0
                num+=1
                continue
        elif color_board[nx][ny]==0:
            flag=0
            temp_index=token_board[x][y].index(num)
            temp_list=token_board[x][y][temp_index:]
            #print("temp_list",temp_list)
            token_board[nx][ny]+=temp_list
            del token_board[x][y][temp_index:]
            for t in temp_list:
                token_list[t][0]=nx
                token_list[t][1]=ny


        elif color_board[nx][ny]==1:
            flag=0
            temp_index = token_board[x][y].index(num)
            temp_list = token_board[x][y][temp_index:]
            #print("temp)list",temp_list)
            temp_list.reverse()
            token_board[nx][ny]+=temp_list
            del token_board[x][y][temp_index:]
            for t in temp_list:
                token_list[t][0] = nx
                token_list[t][1] = ny
        if len(token_board[nx][ny])>=4:
            result=turn
            endflag=1
            break
        num+=1
    if endflag==1:
        break
print(result)
