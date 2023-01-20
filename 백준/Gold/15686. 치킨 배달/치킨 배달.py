from itertools import combinations
import sys
input=sys.stdin.readline
def chk_sum(x,y):
    sum=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]==1:
                sum+=abs(i-x)+abs(j-y)
    return sum

def find_min_length(x,y,arr):
    result=1e9
    for i in arr:
        if abs(i[0]-x)+abs(i[1]-y)<result:
            result=abs(i[0]-x)+abs(i[1]-y)
    return result

n,m= map(int,input().split())
graph=[[-1]*(n+1)]
for i in range(n):
    graph.append([-1]+list(map(int,input().split())))
#print(graph)

chickenlist=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==2:
            chickenlist.append((i,j))
# for i in range(1,m+1):
#     temp=list(combinations(chickenlist,i))
#     print(temp)

result=1e9
for k in range(1,m+1):
    comb=list(combinations(chickenlist,k))
    for temp_chickenlist in comb:
        sum=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j]==1:
                    sum+=find_min_length(i,j,temp_chickenlist)
        if sum<result:
            result=sum
            
print(result)
        