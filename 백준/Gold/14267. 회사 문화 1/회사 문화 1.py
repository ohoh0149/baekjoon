import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m=map(int,input().split())
lst=[0]+list(map(int,input().split()))


p_lst=[0]*(n+1)
for _ in range(m):
    i,w=map(int,input().split())
    p_lst[i]+=w

dp=[0]*(n+1)
#print(lst)
#print(p_lst)
def dfs(num):
    global dp
    #print(num)
    if dp[num]:
        return dp[num]
    parent=lst[num]
    if parent==-1:
        return 0
    dp[num]=dfs(parent)+p_lst[num]
    return dp[num]

for i in range(1,n+1):
    dfs(i)
print(*dp[1:])