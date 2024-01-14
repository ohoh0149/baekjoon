import copy

def solution(triangle):
    answer = 0
    n=len(triangle)
    #print(n)
    dp=copy.deepcopy(triangle)
    #print(dp)
    for i in range(1,n):
        for j in range(i+1):
            #print(i,j)
            if j ==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
    #print(dp)
    answer=max(dp[n-1])
                
    return answer