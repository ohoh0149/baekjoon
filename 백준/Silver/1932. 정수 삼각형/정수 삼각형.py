n= int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
#print(arr)

dp=[[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+arr[i-1][j-1]

max=0
for i in dp:
    for j in i:
        if max<j:
            max=j
print(max)