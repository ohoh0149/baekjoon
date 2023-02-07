n,l=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
#print(graph)




def check_install(arr,visited,cur,l,dir):
    cur_height=arr[cur]
    if cur+dir*(l-1)>=n or cur+dir*(l-1)<0:
        return False
    if dir==1:
        for i in range(cur,cur+l):
            if visited[i]!=0 or arr[i]!= cur_height:
                return False
        visited[cur:cur+l]=[dir]*l
        return True
            
    if dir==-1:
        for i in range(cur,cur-l,-1):
            if visited[i]!=0 or arr[i]!= cur_height:
                return False
        visited[cur-l+1:cur+1]=[dir]*l
        return True


def check_line(arr):
    visited=[0]*len(arr)
    
    i=0
    while i <n-1:
        # print("i",i)
        # if flag==1 and next_cur!=i:
        #     if next_cur==i-1:
        #         flag=0
        #     print("flag",flag)
        #     continue

        if abs(arr[i+1]-arr[i])>1:
            return False
        elif arr[i+1]-arr[i]==0:
            i+=1
            continue
        elif arr[i+1]-arr[i]==1:
            if not check_install(arr,visited,i,l,-1):
                return False
            i+=1
            continue
        elif arr[i+1]-arr[i]==-1:
            if not check_install(arr,visited,i+1,l,1):
                return False
            
            if i+1+l==n:
                return True
            elif arr[i+1+l]-arr[i+l]>0:
                return False
            next_cur=i+l
            
            
        i+=1
    return True
            
count=0
for i in range(n):
    if check_line(graph[i]):
        count+=1
# a=check_install([2,1,1,2,3],[0,0,0,0,0],3,1,1)
# print(a)
for j in range(n):
    temp_arr=[]
    for i in range(n):
        temp_arr.append(graph[i][j])
    if check_line(temp_arr):
        count+=1

print(count)