n,m=map(int,input().split())

input_lst=list(map(int,input().split()))
input_lst.sort()

cur_lst=[]
ans_set=set()
visited=[0]*n
def dfs(k):
    global cur_lst
    if k==m:
        temp=cur_lst.copy()
        ans_set.add(tuple(temp))
        return

    for i in range(n):
        if visited[i]==1:
            continue
        visited[i]=1
        cur_lst.append(input_lst[i])
        dfs(k+1)
        cur_lst.pop()
        visited[i]=0
dfs(0)

lst=list(ans_set)
lst.sort()
for a in lst:
    print(*a)