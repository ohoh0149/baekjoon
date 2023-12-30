import heapq

def solution(scoville, K):
    answer = 0
    q=scoville
    heapq.heapify(q)
    
    while True:
        m=heapq.heappop(q)
        if m<K:
            if len(q)==0:
                answer=-1
                break
            else:
                m2=heapq.heappop(q)
                heapq.heappush(q,m+2*m2)
        else:
            break
        
        answer+=1
            
    
    #print(q)
    
    return answer