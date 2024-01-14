def in_range(x,y):
    return 0<=x<r and 0<=y<c
r,c=-1,-1
def solution(m, n, puddles):
    global r,c
    r=n
    c=m
    answer = 0
    dp=[[0]*m for _ in range(n)]
    dp[0][0]=1
    for x in puddles:
        #print(x,y)
        if x:
            dp[x[1]-1][x[0]-1]=-1
    #print(dp)
    for i in range(n):
        for j in range(m):
            if dp[i][j]==-1:
                continue
            lst=[(i-1,j), (i,j-1)]
            for a,b in lst:
                if in_range(a,b) and dp[a][b]!=-1:
                    dp[i][j]+=dp[a][b]
    #print(dp)
            
    return dp[n-1][m-1]%1000000007