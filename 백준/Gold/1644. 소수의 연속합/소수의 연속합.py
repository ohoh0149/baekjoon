n=int(input())

prime_lst=[]

def is_prime(num):
    if num==2:
        return True
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

for i in range(2,n+1):
    if is_prime(i):
        prime_lst.append(i)
if n==1:
    print(0)
    exit()
if n==2 or n==3:
    print(1)
    exit()


p1=0
p2=1

result=0
sm=prime_lst[p1]+prime_lst[p2]
l=len(prime_lst)
while p2<l:
    if sm<=n:
        if sm==n:
            result+=1
        p2+=1
        if p2==l:
            break
        sm+=prime_lst[p2]
    else:
        sm-=prime_lst[p1]
        p1+=1

print(result)


