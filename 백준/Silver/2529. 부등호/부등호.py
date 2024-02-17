n=int(input())
lst=list(input().split())
#print(n,lst)

max_result="0"*n
min_result="9"*n

visited=[0]*10
def dfs(k,s_num):
    global max_result,min_result,visited
    if s_num:
        if min_result[0]<s_num[0]<max_result[0]:
            return

    if k==n+1:
        max_result=max(max_result,s_num)
        min_result=min(min_result,s_num)
        return

    if s_num:
        for i in range(10):
            if visited[i]!=0:
                continue
            if lst[k-1]=="<" and int(s_num[k-1])<i or lst[k-1]==">" and int(s_num[k-1])>i:
                visited[i]=1
                dfs(k+1,s_num+str(i))
                visited[i]=0
    else:
        for i in range(10):
            visited[i]=1
            dfs(k+1,s_num+str(i))
            visited[i]=0



dfs(0,"")
print(max_result)
print(min_result)