
t=int(input())

for _ in range(t):
    money=0
    n=int(input())
    price_lst=list(map(int,input().split()))
    price_lst.append(0)

    max_lst=[0]*n
    max_val=0
    for i in range(n-1,-1,-1):
        max_lst[i]=max_val
        max_val=max(max_val,price_lst[i])


    cur_count=0
    for i in range(n):
        if max_lst[i]>price_lst[i]:
            cur_count+=1
            money-=price_lst[i]
        else:
            money+=cur_count*price_lst[i]
            cur_count=0
    print(money)

