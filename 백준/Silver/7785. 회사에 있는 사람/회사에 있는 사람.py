n=int(input())
s=set()
for _ in range(n):
    a,b = input().split()
    if b=="enter":
        s.add(a)
    else:
        s.remove(a)

lst=list(s)
lst.sort(reverse=True)
for temp in lst:
    print(temp)