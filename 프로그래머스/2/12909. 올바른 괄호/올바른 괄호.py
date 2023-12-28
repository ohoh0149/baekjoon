def solution(s):
    answer = True
    val=0
    lst=list(s)
    
    for idx,a in enumerate(lst):
        if a==')':
            if val==0:
                return False
            else:
                val-=1
        else:
            val+=1
            
    
    if val==0:
        return True
    else:
        return False