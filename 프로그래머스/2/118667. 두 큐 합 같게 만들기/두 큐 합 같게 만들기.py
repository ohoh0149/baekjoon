from collections import deque
def solution(queue1, queue2):
    answer = -2
    q1=deque(queue1)
    q2=deque(queue2)
    
    s1=sum(q1)
    s2=sum(q2)
    count=0
    while True:
        if s1==s2:
            break
        if count>1000000:
            break
        if s1>s2:
            val=q1.popleft()
            q2.append(val)
            s1-=val
            s2+=val
            
        else:
            val=q2.popleft()
            q1.append(val)
            s1+=val
            s2-=val
            
        count+=1
    if count>1000000:
        return -1
    return count
        
    
    return answer