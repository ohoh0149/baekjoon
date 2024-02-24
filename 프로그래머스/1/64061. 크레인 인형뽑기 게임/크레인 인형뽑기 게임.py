def solution(board, moves):
    answer = 0
    n=len(board)
    lst=[]
    for m in moves:
        m-=1

        for i in range(n):
            if board[i][m]:
                temp=board[i][m]
                board[i][m]=0
                if lst and lst[-1]==temp:
                    lst.pop()
                    answer+=2
                else:
                    lst.append(temp)
                break
    
                    
        
    return answer