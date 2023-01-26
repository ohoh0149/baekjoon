from itertools import combinations
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(input().split()))
#print(graph)
xarr=[]
tarr=[]
sarr=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            xarr.append((i,j))
        elif graph[i][j]=='T':
            tarr.append((i,j))
        elif graph[i][j]=='S':
            sarr.append((i,j))

# S발견하면 return False 발견 못하면 return True
def t_check(r,c): 
    for i in range(4):
        temp_r=r
        temp_c=c
        for j in range(n):
            temp_r+=dx[i]
            temp_c+=dy[i]
            #print(temp_r,temp_c)
            if temp_r>=n or temp_r<0 or temp_c >=n or temp_c <0:
                break
            if graph[temp_r][temp_c]=='O':
                break
            if graph[temp_r][temp_c]=='S':
                return False
    return True
             
        
#print(t_check(3,1))

comb_list=list(combinations(xarr,3))
#print(comb_list)

flag=0
for a,b,c in comb_list:
    #print(a,b,c)
    find_s=0
    graph[a[0]][a[1]]='O'
    graph[b[0]][b[1]]='O'
    graph[c[0]][c[1]]='O'
    for x,y in tarr:
        #print(x,y)
        if t_check(x,y)==False:
            find_s=1
            break
    if find_s==0:
        flag=1
        print("YES")
        break
    




    graph[a[0]][a[1]]='X'
    graph[b[0]][b[1]]='X'
    graph[c[0]][c[1]]='X'
if flag==0:
    print("NO")