from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def in_range(pos):
    x = pos[0]
    y = pos[1]
    return 0 <= x < n and 0 <= y < n


def move(pos1, pos2, d):
    npos1 = (pos1[0] + dx[d], pos1[1] + dy[d])
    npos2 = (pos2[0] + dx[d], pos2[1] + dy[d])
    return npos1, npos2

#앞에 좌표에서 뒤 좌표로 가는 방향
def get_d(pos1,pos2):
    xy = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    d = dxy.index(xy)
    return d
    

def get_next_turn_pos(pos1,pos2,board,val):
    if val==4:
        cpos,npos=check_turn(pos1,pos2,1,board)
    elif val==5:
        cpos,npos=check_turn(pos1,pos2,-1,board)
    elif val==6:
        cpos,npos=check_turn(pos2,pos1,1,board)
    elif val==7:
        cpos,npos=check_turn(pos2,pos1,-1,board)
        
    if npos!=-1:
        return cpos,npos
    return -1,-1
        
    
    
# 중심점 , 회전점, 방향 시계방향 1 반시계 -1

#회전하기 만약 실패하면 False 반환
def check_turn(cpos, pos, c,board):
    xy = (pos[0] - cpos[0], pos[1] - cpos[1])
    d = dxy.index(xy)
    check_pos = pos[0] + dx[(d + 4 + c) % 4], pos[1] + dy[(d + 4 + c) % 4]
    n_pos = cpos[0] + dx[(d + 4 + c) % 4], cpos[1] + dy[(d + 4 + c) % 4]
    if not in_range(check_pos) or board[check_pos[0]][check_pos[1]]==1:
        return -1,-1
    if not in_range(n_pos):
        return -1,-1
    #print(check_pos,n_pos)
    return cpos,n_pos
    
    



n=0

def solution(board):
    global n

    n = len(board) 
    visited = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    # print(move(pos1,pos2,1))
    #check_turn((1,1), pos2, 1,board)
    answer = 0


    print(get_d((1,2),(0,2)))
    q=deque()
    q.append(((0,0),(0,1)))

    visited[0][0][1]=1

    visited[0][1][3]=1


    
    while q:
        pos1,pos2=q.popleft()
        #print(pos1,pos2)
        bdi=get_d(pos1,pos2)
        #그냥 이동하는 경우
        for d in range(8):
            if d<4:
                npos1,npos2=move(pos1,pos2,d)
                di=get_d(npos1,npos2)
            else:
                npos1,npos2=get_next_turn_pos(pos1,pos2,board,d)
                if npos1==-1:
                    continue
                di=get_d(npos1,npos2)
            
            if in_range(npos1) and in_range(npos2) and board[npos1[0]][npos1[1]]==0 and board[npos2[0]][npos2[1]]==0:
                if visited[npos1[0]][npos1[1]][di]==0:
                    q.append((npos1,npos2))
                    visited[npos1[0]][npos1[1]][di]=visited[pos1[0]][pos1[1]][bdi]+1
                    visited[npos2[0]][npos2[1]][(di+2)%4]=visited[pos1[0]][pos1[1]][bdi]+1
                #if visited[npos2[0]][npos2[1]][(di+2)%4]==0:

                
        
        #회전하는 경우
        #pos1회전축 
        
        #pos2회전축
    
#     for i in range(n):
#         print(visited[i])
    answer=1e9
    for i in range(4):
        if visited[n-1][n-1][i]!=0:
            answer=min(visited[n-1][n-1][i],answer)
    #answer=min(visited[n-1][n-1])-1
    answer-=1
    return answer