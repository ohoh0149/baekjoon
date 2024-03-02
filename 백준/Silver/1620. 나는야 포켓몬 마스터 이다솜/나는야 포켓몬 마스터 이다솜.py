n,m=map(int,input().split())
lst=[0]*(n+1)
dic=dict()
for i in range(1,n+1):
    s=input()
    lst[i]=s
    dic[s]=i

for _ in range(m):
    inp=input()
    if inp.isdigit():
        print(lst[int(inp)])
    else:
        print(dic[inp])

