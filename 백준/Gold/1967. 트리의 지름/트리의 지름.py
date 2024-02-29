import  sys
sys.setrecursionlimit(10**4)
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    p,c,w=map(int,input().split())
    graph[p].append([c,w])

# for i in range(1,n+1):
#     print(graph[i])


dp=[[0,0] for _ in range(n+1)]
def dfs(num):
    if not graph[num]:
        dp[num][0]=0
        dp[num][1]=0
        return

    max_val=0
    line_lst=[]
    for c1,w1 in graph[num]:
        dfs(c1)
        max_val=max(max_val,dp[c1][0])
        line_lst.append(dp[c1][1]+w1)
    dp[num][0]=max_val
    line_lst.sort()
    if len(line_lst)==0:
        dp[num][1]=0
    elif len(line_lst)==1:
        dp[num][1]=line_lst[0]
    else:
        dp[num][1]=line_lst[-1]
        dp[num][0]=max(dp[num][0],line_lst[-1]+line_lst[-2])


dfs(1)
# for i in range(1,n+1):
#     print(dp[i])
print(max(dp[1]))