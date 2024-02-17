result=0
def solution(info, edges):
    global result
    n=len(info)
    tree=[[] for _ in range(n)]
    for a,b in edges:
        tree[a].append(b)
    
    visited=[0]*n
    visited[0]=1

    s=set()
    s.add(0)
    def dfs(k,s_count,d_count):

        global result
        result=max(result,s_count)
        if k==n:
            return
        if s_count<=d_count:
            return 
        
        for i in s:
            if tree[i]:
                for x in tree[i]:

                    if visited[x]==0:
                        if info[x]==0:
                            temp_s=s_count+1
                            temp_d=d_count
                        else:
                            temp_d=d_count+1
                            temp_s=s_count
                        visited[x]=1
                        s.add(x)
                        dfs(k+1,temp_s,temp_d)
                        s.remove(x)
                        visited[x]=0
    dfs(0,1,0)
    return result
        
        

    