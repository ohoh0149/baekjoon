from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            answer+=1
            visited[i]=1
            q=deque()
            q.append(i)
            while q:
                x=q.popleft()
                for j in range(n):
                    if visited[j]==0 and computers[x][j]==1:
                        q.append(j)
                        visited[j]=1
    return answer