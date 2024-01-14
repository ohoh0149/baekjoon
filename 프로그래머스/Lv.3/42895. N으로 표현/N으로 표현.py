def solution(N, number):
    if number==N:
        return 1
    answer = 0
    dp=[set([0]),set([N])]

    for i in range(2,9):
        #dp.append(int(str(N)*i)
        
        s=set()
        s.add(int(str(N)*i))
        for j in range(1,i):

            s1=dp[j]
            s2=dp[i-j]
            for a in s1:
                for b in s2:
                    s.add(a+b)
                    s.add(a-b)
                    s.add(a*b)
                    if b!=0:
                        s.add(a//b)
        if number in s:
            return i
        else:
            
            dp.append(s)
        
        
    
    
    return -1