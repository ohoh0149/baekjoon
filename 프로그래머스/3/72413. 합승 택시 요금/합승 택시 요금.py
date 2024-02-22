from collections import deque
# def min_len(v1,v2):
#     visited=[1e9]*(n+1)
#     s=set()
#     q=[]
#     heapq.heappush(q,v1)
#     while q:
#         x=heapq.heappop(q)
#         s.add(x)
#         for nx in range(1,n+1):
#             if arr[x][nx]>0 and nx not in s:
#                 visited[nx]=min(visited[nx],visited[x]+arr[x][nx])
    
INF=1e9

import heapq
def dijkstra(start,end,n):
    q=[]
    distance = [INF]*(n+1)
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start]=0
    #q가 비어있지 않다면
    while q:
        #가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]
    
graph=[]

def solution(n, s, a, b, fares):
    global graph
    graph=[[] for _ in range(n+1)]
    for x,y,z in fares:
        graph[x].append([y,z])
        graph[y].append([x,z])
    #print(graph)
    print(dijkstra(4,5,n))
    
    answer=1e9
    for i in range(1,n+1):
        val=dijkstra(s,i,n)
        val+=dijkstra(i,a,n)
        val+=dijkstra(i,b,n)
        answer=min(answer,val)
        

    return answer