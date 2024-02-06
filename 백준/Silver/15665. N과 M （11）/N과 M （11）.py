n,m=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort()

cur_lst=[]
def dfs(k):
    global cur_lst
    if k==m:
        print(*cur_lst)
        return

    prev=-1
    for i in range(n):
        if prev==lst[i]:
            continue
        prev=lst[i]
        cur_lst.append(lst[i])
        dfs(k+1)
        cur_lst.pop()

dfs(0)