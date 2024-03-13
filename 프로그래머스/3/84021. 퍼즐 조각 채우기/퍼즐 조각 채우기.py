from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=0
def in_range(x,y):
    return 0<=x<n and 0<=y<n


def rotate(pos_lst,l):
    new_pos_lst=[]
    for x,y in pos_lst:
        new_pos_lst.append((y,l-1-x))
    return new_pos_lst

def get_up_left(pos_lst):
    new_pos_lst=[]
    min_x,min_y=1e9,1e9
    max_x,max_y=0,0
    for x,y in pos_lst:
        min_x=min(min_x,x)
        min_y=min(min_y,y)
        max_x=max(max_x,x)
        max_y=max(max_y,y)
    l=max(max_x-min_x,max_y-min_y)+1
    
    for x,y in pos_lst:
        new_pos_lst.append((x-min_x,y-min_y))
    return new_pos_lst,l

def check(pos_lst1,pos_lst2):
    if len(pos_lst1)!=len(pos_lst2):
        return False
    pos_lst1,l1=get_up_left(pos_lst1)
    pos_lst2,l2=get_up_left(pos_lst2)
    if l1!=l2:
        return False
    
    pos_lst1.sort()    
    for d in range(4):
        pos_lst2.sort()
        if pos_lst1==pos_lst2:
            return True
        pos_lst2=rotate(pos_lst2,l2)
        pos_lst2,l2=get_up_left(pos_lst2)
        if d==3:
            break
    
    return False
        
    
    

    

def solution(game_board, table):
    global n
    answer = 0


    
    n=len(game_board)
    pos_lst_lst=[]
    visited=[[0]*n for _ in range(n)]
    
    
    def bfs(x,y,arr,visited,flag):
        pos_lst=[(x,y)]
        q=deque()
        q.append((i,j))
        visited[i][j]=1
        while q:
            x,y=q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if in_range(nx,ny) and arr[nx][ny]==flag and visited[nx][ny]==0:
                    q.append((nx,ny))
                    visited[nx][ny]=1
                    pos_lst.append((nx,ny))
        return pos_lst

    
    pos_lst_lst2=[]
    visited2=[[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if table[i][j]==1 and visited[i][j]==0:
                pos_lst_lst.append(bfs(i,j,table,visited,1))
                
            if game_board[i][j]==0 and visited2[i][j]==0:
                pos_lst_lst2.append(bfs(i,j,game_board,visited2,0))
        
    

    visited=[0]*len(pos_lst_lst)
    for pos_lst2 in pos_lst_lst2:
        for i,pos_lst1 in enumerate(pos_lst_lst):


            if visited[i]:
                continue
            if check(pos_lst2,pos_lst1):

                visited[i]=1
                answer+=len(pos_lst1)

                break
                
        


                

    
    return answer