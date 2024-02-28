from collections import defaultdict

n=int(input())
graph=[[] for _ in range(n+1)]
parent_lst=[0]*(n+1)
for _ in range(n):
    a,l,r=map(int,input().split())
    graph[a].extend([l,r])
    if l!=-1:
        parent_lst[l]=a
    if r!=-1:
        parent_lst[r]=a
for i in range(1,n+1):
    if parent_lst[i]==0:
        route=i
        break

count=0
def inorder(num,depth):
    global count
    l,r=graph[num]
    if l!=-1:
        inorder(l,depth+1)
    count+=1
    min_lst[depth]=min(min_lst[depth],count)
    max_lst[depth]=max(max_lst[depth],count)

    if r!=-1:
        inorder(r,depth+1)

min_lst=[1e9]*(n+1)
max_lst=[0]*(n+1)
inorder(route,1)


max_idx=-1
max_width=0
for i in range(1,n+1):
    if max_lst[i]==0:
        break
    cur_width=max_lst[i]-min_lst[i]+1
    if max_width<cur_width:
        max_idx=i
        max_width=cur_width
print(max_idx,max_width)
