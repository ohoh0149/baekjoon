def solution(N, stages):
    answer = []
    
    index_fail=[]
    
    #stages.sort()
    count_arr=[0]*(N+2)
    print(count_arr)
    temp_len=len(stages)
    for i in stages:
        count_arr[i]+=1
    for i in range(1,N+1):
        if temp_len==0:
            index_fail.append((i,0))
            continue
        index_fail.append((i,count_arr[i]/temp_len))
        temp_len-=count_arr[i]
    #print(index_fail)
    index_fail.sort(key=lambda x:x[1],reverse=True)
    print(index_fail)
    for i,j in index_fail:
        answer.append(i)
        
        
        
    
    return answer