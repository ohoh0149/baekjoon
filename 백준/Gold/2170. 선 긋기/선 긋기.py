import sys
input=sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    if a>b:
        a,b=b,a
    lst.append((a,b))
lst.sort()
lst.append((1e9+1,1e9+1))

result=0
cur_start=-1e9-1
cur_end=-1e9-1
for s,e in lst:
    if cur_end<s:
        result+=int((cur_end-cur_start))
        cur_start=s
        cur_end=e
    else:
        cur_end=max(cur_end,e)
print(result)

