

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    add,sub,mul,div=map(int,input().split())
    arr=list(map(int,input().split()))


    maxresult=-1e9
    minresult=1e9
    def dfs(count,result,addcount,subcount,mulcount,divcount):
        
        global maxresult
        global minresult
        #print(count)
        if count==n:
            
            maxresult=max(maxresult,result)
            minresult=min(minresult,result)
            return
        if addcount+1<=add:
            dfs(count+1,result+arr[count],addcount+1,subcount,mulcount,divcount)
        if subcount+1<=sub:
            dfs(count+1,result-arr[count],addcount,subcount+1,mulcount,divcount)
        if mulcount+1<=mul:
            dfs(count+1,result*arr[count],addcount,subcount,mulcount+1,divcount)
        if divcount+1<=div:
            dfs(count+1,int(result/arr[count]),addcount,subcount,mulcount,divcount+1)

    dfs(1,arr[0],0,0,0,0)
    print("#"+str(test_case),maxresult-minresult)







    # ///////////////////////////////////////////////////////////////////////////////////
