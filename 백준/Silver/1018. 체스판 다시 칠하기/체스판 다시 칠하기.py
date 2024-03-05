n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]

result=1e9
for i in range(n-8+1):
    for j in range(m-8+1):
        cur_result1=0
        cur_result2=0
        count=0
        for a in range(8):
            for b in range(8):
                #a+i,b+j
                color=arr[a+i][b+j]
                if (a+b)%2==0:
                    if color=="B":
                        cur_result1+=1
                    if color=="W":
                        cur_result2+=1
                else:
                    if color=="W":
                        cur_result1+=1
                    if color=="B":
                        cur_result2+=1
                count+=1
        result=min(result,cur_result1,cur_result2)


print(result)