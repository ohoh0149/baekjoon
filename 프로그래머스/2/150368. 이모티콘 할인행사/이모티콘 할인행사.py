answer=[0,0]
def solution(users, emoticons):
    global answer

    n=len(users)
    m=len(emoticons)
    cur_lst=[0]*m
    s_lst=[10,20,30,40]
    
    #가입자수, 총판매액 반환
    def get_result():
        price_lst=[]
        for i in range(m):
            price_lst.append(emoticons[i]*((100-cur_lst[i])/100))
        count=0
        total_price=0
        for i,(ratio,price) in enumerate(users):
            
            cur_price=0
            for i,s in enumerate(cur_lst):
                #구매하는 경우
                if ratio<=s:
                    cur_price+=price_lst[i]
            
            if cur_price>=price:
                count+=1
            else:
                total_price+=cur_price
        return [count,total_price]
        
    
    
    def dfs(k):
        global answer
        if k==m:
            answer=max(answer,get_result())
            return
        for s in s_lst:
            cur_lst[k]=s
            dfs(k+1)
            
    dfs(0)
            
    
        
    
    return answer