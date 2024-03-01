
n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort(reverse=True)

for _ in range(m):
    a=lst.pop()
    b=lst.pop()
    lst.append(a+b)
    lst.append(a+b)
    lst.sort(reverse=True)
    #print(lst)
print(sum(lst))

