n=int(input())
lst=[]
for _ in range(n):
    s,w=map(int,input().split())
    lst.append([s,w])

result=0
def dfs(k,count):
    global result,lst

    if k==n:
        result=max(result,count)
        return
    #손에 든 계란이 깨진 경우
    if lst[k][0] <= 0:
        dfs(k+1,count)
    else:
        flag=False
        for i in range(n):
            if i==k:
                continue
            if lst[i][0]<=0:
                continue
            flag=True
            #k번<->i번
            a,b=lst[k][0],lst[i][0]
            lst[k][0]-=lst[i][1]
            lst[i][0]-=lst[k][1]
            temp_count=0
            if lst[k][0]<=0:
                temp_count+=1
            if lst[i][0]<=0:
                temp_count+=1

            dfs(k+1,count+temp_count)

            lst[k][0],lst[i][0]=a,b
        if not flag:
            dfs(k+1,count)

dfs(0,0)
print(result)
