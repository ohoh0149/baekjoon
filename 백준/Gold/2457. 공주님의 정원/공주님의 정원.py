n=int(input())
lst=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    lst.append([a,b,c,d])
lst.sort(reverse=True)

result=0
m,d=3,1
em,ed=11,30
count=0
while True:
    if (m,d)>(em,ed):
        break
    if not lst:
        result=0
        break
    temp_lst=[]
    while lst:
        if [m,d]>=lst[-1][:2]:
            temp_lst.append(lst.pop())
        else:
            break
    temp_lst.sort(key=lambda x:(x[2],x[3]))
    if not temp_lst:
        result=0
        break
    c,e=temp_lst[-1][2:]
    result+=1
    m,d=c,e

print(result)






