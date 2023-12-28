def solution(progresses, speeds):
    answer = []
    lst=[]
    for idx,(p,s) in enumerate(zip(progresses,speeds)):
        if (100-p)%s==0:
            lst.append((100-p)//s)
        else:
            lst.append((100-p)//s+1)
            
    
    #print(lst)
    
    while lst:
        day=lst.pop(0)
        count=1
        while True:
            if len(lst)>0 and lst[0]<=day:
                lst.pop(0)
                count+=1
            else:
                break
        answer.append(count)
            
        
        
    return answer