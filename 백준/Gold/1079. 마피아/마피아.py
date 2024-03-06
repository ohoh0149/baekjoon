n=int(input())

lst=list(map(int,input().split()))


#불변
arr=[list(map(int,input().split())) for _ in range(n)]

num=int(input())

result=0
visited=[False]*n
def dfs(k,count):
    global result,lst,visited
    result=max(result,count)
    if k==0:
        return
    #밤
    if k%2==0:
        # min_idx=-1
        # min_val=1e9
        # for r in range(n):
        #     if r==num or visited[r]:
        #         continue
        #     if min_val>arr[r][num]:
        #         min_idx=r
        #         min_val=arr[r][num]
        #

        for c in range(n):
            if not visited[c] and c!=num:
                visited[c]=True
                add_lst = arr[c]
                for i, a in enumerate(add_lst):
                    lst[i] += a
                dfs(k-1,count+1)
                for i, a in enumerate(add_lst):
                    lst[i] -= a
                visited[c]=False
    #낮
    else:
        max_idx=-1
        max_val=-1e9
        for i,val in enumerate(lst):
            if not visited[i] and val>max_val:
                max_idx=i
                max_val=val
        if max_idx==num:
            return

        visited[max_idx]=True
        dfs(k-1,count)
        visited[max_idx]=False



dfs(n,0)
print(result)

