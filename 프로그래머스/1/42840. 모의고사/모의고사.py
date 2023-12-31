def solution(answers):
    answer=[]
    count=0
    for i,a in enumerate(answers):
        if (i%5)+1==a:
            count+=1
    answer.append(count)
    
    count=0
    tmp=[1,3,4,5]
    for i,a in enumerate(answers):
        if i%2==0:
            if a==2:
                count+=1
        else:
            j=i//2
            v=tmp[j%4]
            if v==a:
                count+=1
    answer.append(count)
    
    
    count=0
    tmp=[3,1,2,4,5]
    for i,a in enumerate(answers):
        v=tmp[(i//2)%5]
        if a==v:
            count+=1
        
    answer.append(count)
    
    lst=[]
    
    ma=max(answer)
    for i,a in enumerate(answer):
        if a==ma:
            lst.append(i+1)
    #print(lst)
            
    
        
    return lst