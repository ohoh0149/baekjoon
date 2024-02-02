n=int(input())
m=int(input())
if m>0:
    s=set(map(int,input().split()))


min_count=abs(100-n)

for nums in range(1000001):
    nums=str(nums)
    break_flag=False
    for a in nums:
        if m>0 and int(a) in s:
            break_flag=True
            break
    if break_flag:
        continue
    min_count=min(min_count,len(nums)+abs(int(nums)-n))
print(min_count)