n=int(input())

def in_range(x):
    return 0<=x<10
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[1]*10
dp[1][0]=0

for i in range(2,n+1):
    for j in range(10):
        temp_lst=[j-1,j+1]
        for temp in temp_lst:
            if in_range(temp):
                dp[i][j]+=dp[i-1][temp]
print(sum(dp[n])%1000000000)
