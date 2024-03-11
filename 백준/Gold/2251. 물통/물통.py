max_a,max_b,max_c=map(int,input().split())

a,b,c=0,0,max_c

flag=False
count=0
result_set=set()

temp_set=set()
def dfs(a,b,c):

    global flag,result_set,temp_set
    if (a,b,c) in temp_set:
        return
    temp_set.add((a,b,c))

    if a==0:
        result_set.add(c)

    if a>0:
        if max_b-b>=a:
            dfs(0,b+a,c)
        else:
            dfs(a-(max_b-b),max_b,c)

        if max_c-c>=a:
            dfs(0,b,c+a)
        else:
            dfs(a-(max_c-c),b,max_c)

    if b > 0:
        if max_c - c >= b:
            dfs(a, 0, c+b)
        else:
            dfs(a, b-(max_c-c), max_c)

        if max_a - a >= b:
            dfs(a+b, 0, c)
        else:
            dfs(max_a, b-(max_a-a), c)

    if c > 0:
        if max_b - b >= c:
            dfs(a, b + c, 0)
        else:
            dfs(a , max_b, c-(max_b-b))

        if max_a - a >= c:
            dfs(a+c, b, 0)
        else:
            dfs(max_a, b, c-(max_a-a))



dfs(0,0,c)
result_set=list(result_set)
result_set.sort()
print(*result_set)
