n=int(input())

lst=[]
for _ in range(n):
    s,e=map(int,input().split())
    lst.append([s,e])
lst.sort(key=lambda x:(x[1],x[0]),reverse=True)
result=0
cur_time=0
while lst:
    s,e=lst.pop()

    if s>=cur_time:
        result+=1
        cur_time=e
print(result)


