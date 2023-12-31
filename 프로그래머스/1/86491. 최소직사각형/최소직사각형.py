def solution(sizes):
    answer = 0
    ma,mb=-1,-1
    for a,b in sizes:
        ma=max(ma,max(a,b))
        mb=max(mb,min(a,b))
    answer=ma*mb
    return answer