import heapq
def solution(jobs):
    answer = 0
    cur_time=0
    q=[]
    #소요시간, 요청시점
    for a,b in jobs:
        heapq.heappush(q,(b,a))
    while q:
        
        lst=[]
        #ms,mt=1e9,1e9
        mt=1e9
        while True:
            if len(q)==0:
                cur_time=mt
                break
            s,t=heapq.heappop(q)
            mt=min(mt,t)
            if cur_time>=t:
                #print(s,t,cur_time)
                answer+=(cur_time+s-t)
                cur_time+=s
                break
            else:
                lst.append((s,t))
        for s,t in lst:
            heapq.heappush(q,(s,t))
            
                
            

    answer=answer//len(jobs)
    return answer



