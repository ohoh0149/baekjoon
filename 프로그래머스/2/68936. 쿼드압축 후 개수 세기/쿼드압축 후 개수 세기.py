def solution(arr):
    answer = [0,0]

    def dfs(arr):
        if len(arr)==1:
            answer[arr[0][0]]+=1
            return
        n=len(arr)
        s=0
        for i in range(n):
            s+=sum(arr[i])

        if s==0:
            answer[0]+=1
            return
        elif s==n*n:
            answer[1]+=1
            return
        else:
            pos_lst=[(0,0),(n//2,0),(0,n//2),(n//2,n//2)]
            for x,y in pos_lst:
                temp_arr=[]
                for i in range(n//2):
                    temp_lst=[]
                    for j in range(n//2):
                        temp_lst.append(arr[x+i][y+j])
                    temp_arr.append(temp_lst)
                dfs(temp_arr)

                
                
            
            

    dfs(arr)

    return answer