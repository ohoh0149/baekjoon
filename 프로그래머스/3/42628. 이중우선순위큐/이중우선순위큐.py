import heapq
def solution(operations):
    answer = []
    s=set()
    minq=[]
    maxq=[]
    for query in operations:
        typ,num=query[0],int(query[2:])
        if typ=="I":
            s.add(num)
            heapq.heappush(minq,num)
            heapq.heappush(maxq,-num)
        elif typ=="D" and s:
            if num==1:
                while True:
                    m=-heapq.heappop(maxq)
                    if m in s:
                        break
            elif num==-1:
                while True:
                    m=heapq.heappop(minq)
                    if m in s:
                        break
            if m in s:
                s.remove(m)
        #print(minq,maxq,s)
    if not s:
        return [0,0]
    answer=[max(s),min(s)]
            
    return answer