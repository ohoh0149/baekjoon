n,k=map(int,input().split())
lst=[]
for _ in range(n):
    inp=input()
    #lst.append(inp[4:-4])
    st=inp[4:-4]
    new_s=""
    for s in st:
        if s not in ["a","n","t","i","c"]:
            new_s+=s
    lst.append(new_s)



k-=5
if k<0:
    print(0)
    exit()
elif k==0:
    count=0
    for s in lst:
        if s=="":
            count+=1
    print(count)
    exit()

s_set=set()
for st in lst:
    for s in st:
        s_set.add(s)
s_lst=list(s_set)
l=len(s_lst)
cur_lst=[]
max_result=0
def get_result():
    cur_result=0
    for st in lst:
        flag=True
        for s in st:
            if s not in cur_lst:
                flag=False
                break
        if flag:
            cur_result+=1
    return cur_result



def dfs(u,count):
    global max_result
    global cur_lst
    if u==l:
        if count==k:
            max_result=max(max_result,get_result())
        return

    dfs(u+1,count)
    cur_lst.append(s_lst[u])
    dfs(u+1,count+1)
    cur_lst.pop()

if k>l:
    print(len(lst))
else:
    dfs(0,0)
    print(max_result)