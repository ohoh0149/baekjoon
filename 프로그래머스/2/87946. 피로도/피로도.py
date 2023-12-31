from itertools import permutations
def get_count(per,k,dungeons):
    
    temp=k
    count=0
    for i in per:
        a,b=dungeons[i]
        if temp>=a:
            temp-=b
            count+=1
        else:
            break
    return count
        
        
        
        

def solution(k, dungeons):
    answer = -1
    #각 던전마다 최소 필요 피로도, 소모피로도
    #하루에 한번
    l=len(dungeons)
    per_lst=list(permutations(range(l),l))
    for per in per_lst:
        #print(per)
        answer=max(answer,get_count(per,k,dungeons))
    
    return answer