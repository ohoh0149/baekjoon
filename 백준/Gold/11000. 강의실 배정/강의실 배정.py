import heapq

n=int(input())
lst=[]
for _ in range(n):
    s,t=map(int,input().split())
    lst.append((s,t))

lst.sort()

a,b=lst.pop(0)
max_count=0
q=[]
count=1
heapq.heappush(q,(b,a))
for s,e in lst:
    while q:
        end,start=heapq.heappop(q)
        if s<end:
            heapq.heappush(q,(end,start))
            heapq.heappush(q,(e,s))
            count+=1
            max_count=max(max_count,count)
            break
        else:
            count-=1
            continue

max_count=max(max_count,count)
print(max_count)

