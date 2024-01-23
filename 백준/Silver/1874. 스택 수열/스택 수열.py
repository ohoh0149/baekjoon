n=int(input())
lst=[]
k=1
ans_lst=[]
flag=False
for _ in range(n):
    a=int(input())
    #print("a",a)
    while True:
        if k==a:
            ans_lst.append("+")
            ans_lst.append("-")
            #print(1,k)
            k+=1
            break
        if k<a:
            ans_lst.append("+")
            lst.append(k)
            k+=1
        elif k>a:
            ans_lst.append("-")
            var=lst.pop()
            #print(2,var)
            if var!=a:
                flag=True
            break
    if flag:
        break

#print(ans_lst)
if flag:
    print("NO")
else:
    for temp in ans_lst:
        print(temp)







