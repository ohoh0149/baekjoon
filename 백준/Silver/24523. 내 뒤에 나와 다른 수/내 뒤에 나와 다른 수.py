n=int(input())
lst=list(map(int,input().split()))


stack=[]

result_lst=[-1]*(n+1)
for idx,num in enumerate(lst):
    if not stack:
        stack.append((num,idx+1))
        continue

    while stack:
        if stack[-1][0]!=num:
            cur_num,cur_idx=stack.pop()
            result_lst[cur_idx]=idx+1
        else:
            break
    stack.append((num,idx+1))

print(*result_lst[1:])
