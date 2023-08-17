def cal(num1,num2,t):
    if t==0:
        return num1+num2
    elif t==1:
        return num1-num2
    elif t==2:
        return num1*num2
    elif t==3:
        if num1>0:
            return num1//num2
        else:
            return -((-num1)//num2)


def dfs(k,val):
    global max_result
    global min_result
    if k==n-1:
        max_result=max(max_result,val)
        min_result=min(min_result,val)
        return
    for i in range(4):
        if c_lst[i]>0:
            c_lst[i]-=1
            dfs(k+1,cal(val,a_lst[k+1],i))
            c_lst[i]+=1


n=int(input())
a_lst=list(map(int,input().split()))
c_lst=list(map(int,input().split()))

min_result=1e10
max_result=-1e10
dfs(0,a_lst[0])
print(max_result)
print(min_result)