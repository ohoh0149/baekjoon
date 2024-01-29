import sys
import heapq
input=sys.stdin.readline

q1=[]
q2=[]

n=int(input())
for turn in range(n):
    num = int(input())

    if turn%2==0:
        heapq.heappush(q1,-num)
    else:
        heapq.heappush(q2,num)

    if turn==0:
        print(num)
        continue

    if q2 and -q1[0]>q2[0]:
        num1=-heapq.heappop(q1)
        num2=heapq.heappop(q2)

        heapq.heappush(q1,-num2)
        heapq.heappush(q2,num1)

    # num1=-heapq.heappop(q1)
    # num2=heapq.heappop(q2)
    # if num1>num2:
    #     heapq.heappush(q1,-num2)
    #     heapq.heappush(q2,num1)
    # else:
    #     heapq.heappush(q1,-num1)
    #     heapq.heappush(q2,num2)

    print(-q1[0])





# print(q1)
# print(q2)
