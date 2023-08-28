def solution(brown, yellow):
    answer = []
    #n+m
    a=(brown+4)//2
    #n*m
    b=yellow+2*a-4
    #(n-m)^2
    c=a*a-4*b
    d=int(pow(c,1/2))
    answer=[(a+d)//2,(a-d)//2]
    
    return answer

