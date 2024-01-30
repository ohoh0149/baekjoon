n=int(input())
lst=[0]
for _ in range(n):
    num=int(input())
    lst.append(num)

# same_num_lst=[]
# for i in range(1,n+1):
#     if i==lst[i]:
#         same_num_lst.append(i)


idx_set=set()
num_set=set()
def dfs(idx):
    global idx_set,num_set,visited
    if visited[idx]==1:
        return
    visited[idx]=1
    idx_set.add(idx)
    num_set.add(lst[idx])
    dfs(lst[idx])


result_set=set()
for i in range(1,n+1):
    visited=[0]*(n+1)
    idx_set=set()
    num_set=set()
    dfs(i)
    # print(idx_set)
    # print(num_set)
    # print()
    if idx_set==num_set :
        for a in idx_set:
            result_set.add(a)
#print(result_set)
# for a in same_num_lst:
#     result_set.add(a)

temp_lst=list(result_set)
temp_lst.sort()
print(len(temp_lst))
for a in temp_lst:
    print(a)
