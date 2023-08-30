def dfs(k,string):
    global cnt
    global result
    if result!=0:
        return
    if string==w:
        result=cnt
        return
    if k==5:
        return
    
    for i in range(5):
        cnt+=1
        dfs(k+1,string+lst[i])

lst=["A","E","I","O","U"]
cnt=0
result=0
w=""
def solution(word):
    global cnt
    global w
    w=word
    
    
    dfs(0,"")
    answer=result
    return answer