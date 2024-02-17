n,d,k,c=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))
lst=lst+lst.copy()
result=0
for i in range(n):
    s=set(lst[i:i+k])
    s.add(c)
    result=max(result,len(s))
print(result)
