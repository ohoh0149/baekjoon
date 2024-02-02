n=int(input())
lst=list(map(int,input().split()))

visited=[0]*n
ans_lst=[0]*n
result=-1e9
def dfs(k):
    global visited,ans_lst,result
    if k==n:
        temp=0
        for i in range(n-1):
            temp+=abs(lst[ans_lst[i]]-lst[ans_lst[i+1]])
        result=max(result,temp)
        return

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            ans_lst[k]=i
            dfs(k+1)
            ans_lst[k]=0
            visited[i]=0

dfs(0)
print(result)