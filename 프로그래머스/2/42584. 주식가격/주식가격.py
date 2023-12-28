def solution(prices):
    answer = [0]*len(prices)
    lst=[]
    for idx, p in enumerate(prices):
        lst.append((p,idx))
    #print(lst)
    stack=[]
    for i,(p,idx) in enumerate(lst):
        while True:
            if len(stack)==0:
                break
            if stack[-1][0]<=p:
                break
            else:
                a,b=stack.pop()
                answer[b]=i-b
        stack.append((p,idx))
    
    #print(stack)
    l=len(prices)
    while stack:
        p,idx=stack.pop()
        answer[idx]=l-idx-1
                
            
        
    #1 2 3 2 1 4 3
    #6 
    return answer