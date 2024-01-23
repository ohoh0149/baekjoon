from collections import deque

n=int(input())

q=deque([i+1 for i in range(n)])
#print(q)

while True:
    if len(q)==1:
        break
    q.popleft()
    q.append(q.popleft())

print(q[0])

