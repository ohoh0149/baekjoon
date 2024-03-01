n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

minus_lst=[]
plus_lst=[]
for num in lst:
    if num>0:
        plus_lst.append(num)
    else:
        minus_lst.append(num)

plus_lst.sort()
minus_lst.sort(reverse=True)



result_lst=[]
while True:
    if len(plus_lst)>=2:
        a=plus_lst.pop()
        b=plus_lst.pop()
        if a==1 or b==1:
            result_lst.append(a)
            result_lst.append(b)
        else:
            result_lst.append(a*b)
    else:
        result_lst.extend(plus_lst)
        break

while True:
    if len(minus_lst)>=2:
        a=minus_lst.pop()
        b=minus_lst.pop()
        result_lst.append(a*b)
    else:
        result_lst.extend(minus_lst)
        break

print(sum(result_lst))