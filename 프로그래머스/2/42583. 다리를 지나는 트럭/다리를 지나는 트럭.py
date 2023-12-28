from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_weight=0
    count=0
    truck_count=len(truck_weights)
    q1=deque()
    q2=deque(truck_weights)
    while True:
        if count==truck_count:
            break
        if len(q1)>0:
            if answer-q1[0][1]==bridge_length:
                #print(q1)
                w,t=q1.popleft()
                
                total_weight-=w
                count+=1
        if len(q2)>0:
            if total_weight+q2[0]<=weight:
                w=q2.popleft()
                q1.append((w,answer))
                total_weight+=w
            else:
                answer=bridge_length+q1[0][1]-1
                
        answer+=1

        
    return answer