def solution(n, costs):
    answer = 0
    count=1
    graph=[[0]*n for _ in range(n)]
    for x,y,cost in costs:
        graph[x][y]=cost
        graph[y][x]=cost


        
    s=set([0])
    while True:
        if count==n:
            break
        min_cost, min_v=1e9,1e9
        for v in s:
            for i in range(n):
                if i in s:
                    continue
                if graph[v][i]!=0 and graph[v][i]<min_cost:
                    min_cost=graph[v][i]
                    min_v=i
        s.add(min_v)
        answer+=min_cost
        #print(min_cost,min_v)
        count+=1
        
            
    return answer