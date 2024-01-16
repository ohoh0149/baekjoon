

answer=0
def solution(n):
    global answer
    def check(ss):
        lcount=0
        for s in ss:
            if s=="(":
                lcount+=1
            else:
                if lcount==0:

                    return 0
                else:
                    lcount-=1
        #print(ss)
        return 1
    answer = 0
    lr=[n,n]
    def dfs(k,st):
        global answer
        if k==2*n:
            #print(st)
            answer+=1
            return
        if lr[0]>lr[1]:
            return
        if lr[0]>0:
            lr[0]-=1
            dfs(k+1,st+"(")
            lr[0]+=1
        if lr[1]>0:
            lr[1]-=1
            dfs(k+1,st+")")
            lr[1]+=1
            
    dfs(0,"")
    
    return answer