def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    #print(citations)
    
    for h in range(1,100000):

        if len(citations)>=h and citations[h-1]>=h:
            continue
        else:
            answer=h-1
            break
        #answer=h
        
    return answer