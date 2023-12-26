def solution(participant, completion):
    dic=dict()
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1

    for c in completion:
        dic[c]-=1
    
    for p in participant:
        if dic[p]==1:
            return p
    