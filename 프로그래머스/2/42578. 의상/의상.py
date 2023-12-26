from itertools import combinations
def solution(clothes):
    answer = 0
    dic=dict()
    for a,typ in clothes:
        if typ not in dic:
            dic[typ]=1
        else:
            dic[typ]+=1

    dic2=dict()
    for key,value in dic.items():
        if value not in dic2:
            dic2[value]=1
        else:
            dic2[value]+=1
    
    #print(dic)

    result=1
    for key in dic:
        result*=(dic[key]+1)
    return result-1
        
    l=len(dic)
    for i in range(1,l+1):
        comb_lst=list(combinations(dic.keys(),i))
        for comb in comb_lst:
            result=1
            for k in comb:
                result*=dic[k]
            answer+=result
    return answer