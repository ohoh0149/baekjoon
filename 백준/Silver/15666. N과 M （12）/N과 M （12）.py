n,m=map(int,input().split())
lst=list(map(int,input().split()))

lst.sort()

cur_lst=[]

def dfs(k,last):
    if k==m:
        print(*cur_lst)
        return

    prev=-1
    for i in range(last,n):
        if prev==lst[i]:
            continue
        prev=lst[i]
        cur_lst.append(lst[i])
        dfs(k+1,i)
        cur_lst.pop()

dfs(0,0)