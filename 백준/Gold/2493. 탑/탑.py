n=int(input())
lst=list(map(int,input().split()))


ans_lst=[0]*n

stack=[]
for i in range(n-1,-1,-1):
    #print(i,lst[i])

    while stack:
        h,idx=stack.pop()

        if h<lst[i]:
            ans_lst[idx]=i+1
        else:
            stack.append((h,idx))
            break
    stack.append((lst[i],i))
print(*ans_lst)