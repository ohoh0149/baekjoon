def bomb():
    global arr
    global answer
    flag=False
    remove_arr=[[0]*c for _ in range(r)]
    for i in range(r-1):
        for j in range(c-1):
            if arr[i][j]==0:
                continue
            if arr[i][j]==arr[i+1][j]==arr[i+1][j+1]==arr[i][j+1] :
                remove_arr[i][j],remove_arr[i+1][j+1],remove_arr[i][j+1],remove_arr[i+1][j]=1,1,1,1
                flag=True
        

    for i in range(r):
        for j in range(c):
            if remove_arr[i][j]==1:
                answer+=1
                arr[i][j]=0
    return flag
                

            
    

def move_down():
    global arr
    new_arr=[[0]*c for _ in range(r)]
    
    for j in range(c):
        lst=[]
        for i in range(r-1,-1,-1):
            if arr[i][j]!=0:
                lst.append(arr[i][j])
        
        idx=r-1
        for s in lst:
            new_arr[idx][j]=s
            idx-=1
    arr=new_arr
            
            
    


answer=0
arr=[]
r,c=0,0
def solution(m, n, board):
    global arr,r,c
    r,c=m,n
    for i in range(m):
        lst=[]
        for j in range(n):
            lst.append(board[i][j])
        arr.append(lst)
    
    
    while True:
        if bomb():
            move_down()
        else:
            break
            
            
            
    return answer