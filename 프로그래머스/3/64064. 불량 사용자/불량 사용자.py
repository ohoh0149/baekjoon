n=0

result=0
id_lst=[]
ban_lst=[]
visited=[]

def check(id1,id2):

    if len(id1)!=len(id2):
        return False
    
    for a,b in zip(id1,id2):
        if a!=b and not (a=="*" or b=="*"):
            return False
    return True

s=set()
def dfs(k):

    global result,s
    if k==n:
        #print(visited)
        s.add(tuple(visited))
        return
    
    ban_id=ban_lst[k]
    
    for idx,user in enumerate(id_lst):

        if visited[idx]==0 and check(user,ban_id):
            visited[idx]=1
            dfs(k+1)
            visited[idx]=0
    
    
        

def solution(user_id, banned_id):
    global n,id_lst,ban_lst,visited,result
    id_lst=user_id
    ban_lst=banned_id
    visited=[0]*len(user_id)

    n=len(banned_id)
    
    dfs(0)

    return len(s)
    
    
