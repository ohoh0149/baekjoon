import heapq,sys
input=sys.stdin.readline
n=int(input())

pq=[]
for _ in range(n):
    x=int(input())
    if x!=0:
        heapq.heappush(pq,(abs(x),x))
    else:
        if pq:
            _,a=heapq.heappop(pq)
            print(a)
        else:
            print(0)
