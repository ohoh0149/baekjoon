n=int(input())
lst=list(map(int,input().split()))

ans=[-1]*n

stack=[]
for idx,num in enumerate(lst):
    #print(stack)
    if not stack:
        stack.append((num,idx))
        continue

    while stack:
        if stack[-1][0]>=num:
            break
        else:
            _,b=stack.pop()
            ans[b]=num
    stack.append((num,idx))
print(*ans)