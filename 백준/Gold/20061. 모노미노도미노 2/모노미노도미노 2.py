import sys
input=sys.stdin.readline

def in_range(x,y):
    return 0<=x<6 and 0<=y<4

def put_block(board,pos_lst):
    for _ in range(1,6):
        end_flag=False
        npos_lst=[]
        for x,y in pos_lst:
            npos_lst.append((x+1,y))

        for x,y in npos_lst:
            if not in_range(x,y) or board[x][y]==1:
                end_flag=True
                break
        if end_flag:
            break
        pos_lst=npos_lst

    for x,y in pos_lst:
        board[x][y]=1

def remove_line(board,row):
    for i in range(row-1,-1,-1):
        for j in range(4):
            board[i+1][j]=board[i][j]



def remove_all_line(board):
    point=0
    for i in range(2,6):
        flag=True
        for j in range(4):
            if board[i][j]==0:
                flag=False
        if flag:
            point+=1
            remove_line(board,i)

    return point

def check_board(board):
    lst=[]
    for j in range(4):
        if board[0][j]==1:
            lst.append(4)
            lst.append(5)
            break

    if len(lst)==0:
        for j in range(4):
            if board[1][j]==1:
                lst.append(5)
                break

    for val in lst:
        remove_line(board,val)

    for i in range(2):
        for j in range(4):
            board[i][j]=0


def print_board(board):
    for i in range(0,6):
        print(board[i])
    print()


n=int(input())
green_board=[[0]*4 for _ in range(6)]
blue_board=[[0]*4 for _ in range(6)]
green_result=0
blue_result=0
for _ in range(n):
    t,x,y=map(int,input().split())
    if t==1:
        green_pos_lst=[(0,y)]
        blue_pos_lst=[(0,x)]
    elif t==2:
        green_pos_lst = [(0, y),(0,y+1)]
        blue_pos_lst = [(0, x),(1,x)]
    elif t==3:
        green_pos_lst = [(0, y),(1,y)]
        blue_pos_lst = [(0, x),(0,x+1)]
    put_block(green_board,green_pos_lst)
    put_block(blue_board,blue_pos_lst)
    while True:
        point=remove_all_line(green_board)
        if point==0:
            break
        green_result+=point
    while True:
        point=remove_all_line(blue_board)
        if point==0:
            break
        blue_result+=point
    #print("green")
    check_board(green_board)
    check_board(blue_board)

# print(green_result)
# print(blue_result)
    #print_board(green_board)
    #print("blue")
    #print_board(blue_board)

print(green_result+blue_result)
green_count=0
blue_count=0
for i in range(2,6):
    for j in range(4):
        if green_board[i][j]==1:
            green_count+=1
        if blue_board[i][j]==1:
            blue_count+=1
print(green_count+blue_count)

#
# put_block(green_board,[(0,1),(0,2)])
# print(green_board)
# put_block(green_board,[(0,1),(0,2)])
# put_block(green_board,[(0,2),(0,3)])
# print(green_board)