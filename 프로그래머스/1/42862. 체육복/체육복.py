def solution(n, lost, reserve):
    answer=n-len(lost)
    s=set(reserve)
    lost.sort()
    reserve.sort()
    for num in lost[:]:
        if num in s:
            lost.remove(num)
            s.remove(num)
            answer+=1
            
    for num in lost:
        
        if num-1 in s:
            answer+=1
            s.remove(num-1)
            continue
        if num+1 in s:
            answer+=1
            s.remove(num+1)
            continue

        
        
    return answer