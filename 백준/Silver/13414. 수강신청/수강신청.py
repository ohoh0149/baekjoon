from collections import defaultdict
k,l=map(int,input().split())
dic=defaultdict(int)
for i in range(1,l+1):
    s=input()
    dic[s]=i
dic=sorted(dic,key=lambda x:dic[x])
if len(dic)<=k:
    for temp in dic:
        print(temp)
else:
    for i in range(k):
        print(dic[i])