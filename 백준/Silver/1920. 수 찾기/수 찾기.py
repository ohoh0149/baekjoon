n=int(input())
se=set(map(int,input().split()))
m=int(input())
lst2=list(map(int,input().split()))

for a in lst2:
    if a in se:
        print(1)
    else:
        print(0)

