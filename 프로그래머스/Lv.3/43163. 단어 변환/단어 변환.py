def can_change(word1,word2):
    count=0
    for a,b in zip(word1,word2):
        if a!=b:
            count+=1
        if count>=2:
            return False
    if count==1:
        return True
    else:
        return False
        

def dfs(cur,count,target,words):
    global visited,answer
    if count>=answer:
        return
    if cur==target:
        answer=min(answer,count)
        return
    
    for idx,word in enumerate(words):
        if visited[idx]==0 and can_change(cur,word):
            visited[idx]=1
            dfs(word,count+1,target,words)
            visited[idx]=0
            
        
    

visited=[]
answer=1e9
n=0
def solution(begin, target, words):
    if target not in words:
        return 0
    global visited,answer,n
    visited=[0]*len(words)
    n=len(words)
    
    dfs(begin,0,target,words)
    if answer==1e9:
        return 0
    return answer