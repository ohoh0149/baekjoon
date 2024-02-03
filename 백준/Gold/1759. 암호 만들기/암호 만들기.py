l,c=map(int,input().split())
lst=list(input().split())
lst.sort()

cur_lst=[]
def dfs(k,count):
    if k==c:
        if count==l :
            aCount=0
            bCount=0
            for temp in cur_lst:
                if temp in ["a","e","i","o","u"]:
                    aCount+=1
                else:
                    bCount+=1
            if aCount>=1 and bCount>=2:
                print("".join(cur_lst))
        return
    cur_lst.append(lst[k])
    dfs(k+1,count+1)
    cur_lst.pop()
    dfs(k+1,count)

dfs(0,0)