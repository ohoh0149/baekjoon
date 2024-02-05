n,m=map(int,input().split())

input_lst=list(map(int,input().split()))
input_lst.sort()

cur_lst=[]
def dfs(k):
    global cur_lst
    if k==m:
        print(*cur_lst)
        return

    for i in range(n):
        cur_lst.append(input_lst[i])
        dfs(k+1)
        cur_lst.pop()
dfs(0)

