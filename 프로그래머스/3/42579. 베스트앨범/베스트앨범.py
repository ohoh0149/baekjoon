def solution(genres, plays):
    answer = []
    dic1=dict()
    dic2=dict()
    l=len(plays)
    for i in range(l):
        g=genres[i]
        p=plays[i]
        if g not in dic2:
            dic2[g]=p
        else:
            dic2[g]+=p
        
        if g not in dic1:
            dic1[g]=[(p,-i)]
        else:
            dic1[g].append((p,-i))
    #print(dic1)
    #print(dic2)
    
    lst=[]
    for key in dic2:
        lst.append((dic2[key],key))
    lst.sort(reverse=True)
    
    for key in dic1:
        dic1[key].sort(reverse=True)
    #print(dic1)
    
    for _,t in lst:
        for i in range(min(2,len(dic1[t]))):
            answer.append(-dic1[t][i][1])
        
        
        
        
    return answer