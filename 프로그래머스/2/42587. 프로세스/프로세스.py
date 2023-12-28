from collections import deque

def solution(priorities, location):
    answer = 0
    lst=deque()
    dic=dict()
    dic[-1]=0
    for idx,p in enumerate(priorities):
        if p not in dic:
            dic[p]=1
        else:
            dic[p]+=1
        lst.append((p,idx))
    #print(dic)
    #print(lst)
    #dic=dict()
    #dic[-1]=0
    #print(max(dic.keys()))
    
    while lst:
        p,idx=lst.popleft()
        dic[p]-=1
        if dic[p]==0:
            del dic[p]
        if max(dic.keys())>p:
            lst.append((p,idx))
            if p not in dic:
                dic[p]=1
            else:
                dic[p]+=1
        else:
            answer+=1
            if idx==location:
                return answer
        
        
        
        
    return answer