n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

lst.sort()

min_val=10000
k=0
max_w=0
while lst:
    val=lst.pop()
    k+=1
    min_val=min(min_val,val)
    w=k*min_val
    max_w=max(max_w,w)
print(max_w)

