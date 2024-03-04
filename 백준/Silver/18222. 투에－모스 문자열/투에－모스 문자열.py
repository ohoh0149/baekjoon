k=int(input())
def fun(x):
    if x==0:
        return 0
    if x==1:
        return 1
    if x%2==0:
        return fun(x//2)
    else:
        return 1-fun((x-1)//2)

print(fun(k-1))