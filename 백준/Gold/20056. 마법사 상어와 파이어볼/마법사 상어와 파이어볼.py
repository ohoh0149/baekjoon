n,m,k= map(int,input().split())

graph=[[[]*n for i in range(n)]for i in range(n)]
# print(graph)
for i in range(m):
    r,c,m,s,d=map(int,input().split())
    graph[r-1][c-1].append([m,s,d])
    # print(graph)
# print(graph)

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
def move(graph):
    return_graph=[[[]*n for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            for m,s,d in graph[i][j]:
                nx=(i+s*(dx[d]))%n
                ny=(j+s*(dy[d]))%n
                #print(i,j,nx,ny)
                return_graph[nx][ny].append([m,s,d])
    return return_graph
                

for i in range(k):
    graph=move(graph)
    # for i in range(n):
    #     print(graph[i])
    for i in range(n):
        for j in range(n):
            if len(graph[i][j])>=2:
                
                sum_m=0
                sum_s=0
                count=0
                four_list=[]
                all_even_odd=0
                flag=graph[i][j][0][2]%2
                for m,s,d in graph[i][j]:
                    count+=1
                    sum_m+=m
                    sum_s+=s
                    if d%2 != flag:
                        all_even_odd=1
                graph[i][j]=[]
                for l in range(4):
                    if sum_m//5>0:
                        four_list.append([sum_m//5,sum_s//count,l*2+all_even_odd])
                
                graph[i][j]=four_list
            
result=0
for i in graph:
    for j in i:
        for s,a,b in j:
            result+=s

print(result)
      
                

                