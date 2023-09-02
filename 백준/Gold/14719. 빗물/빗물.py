def get_max(idx):
    if idx==0:
        a=-1
    else:
        a=max(lst[:idx])
    if idx==w-1:
        b=-1
    else:
        b=max(lst[idx+1:])
    return a,b


h,w=map(int,input().split())
lst=list(map(int,input().split()))
lr_lst=[]

for i in range(w):
    lr_lst.append(get_max(i))

result=0
for i in range(w):
    val=min(lr_lst[i])-lst[i]
    if val>0:
        result+=val
print(result)
