def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    n=len(onboard)
    dp=[[1e9]*1000 for _ in range(n)]
    dp[0][temperature]=0
    if t2<temperature:
        good=-1
        summer=True
    else:
        good=1
        summer=False
    
    for i in range(1,n):
        if onboard[i]:
            s,e=t1,t2
        else:
            s,e=-10,40
        for j in range(s,e+1):
            if j==temperature:
                dp[i][j]=min(dp[i][j],dp[i-1][j])
            else:
                dp[i][j]=min(dp[i][j],dp[i-1][j]+b)
            dp[i][j]=min(dp[i][j],dp[i-1][j+good],dp[i-1][j-good]+a)


    


    # for i in range(n):
    #     for j in range(-10,41):
    #         if dp[i][j]==1e9:
    #             print(0,end=" ")
    #         else:
    #             print(dp[i][j],end=" ")
    #     print()


    answer=min(dp[n-1])
    
    return answer