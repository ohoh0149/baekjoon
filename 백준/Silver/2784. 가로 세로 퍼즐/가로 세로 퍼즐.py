s_lst=[]
for _ in range(6):
    s_lst.append(input())


def check():
    new_lst=cur_lst.copy()
    for j in range(3):
        s=""
        for i in range(3):
            s+=cur_lst[i][j]
        new_lst.append(s)
    new_lst.sort()
    if new_lst==s_lst:
        return True



visited=[0]*6
cur_lst=[]
def dfs(k):
    global visited,cur_lst
    if k==3:
        if check():
            for a in cur_lst:
                print(a)
            exit()
        return

    for i in range(6):
        if visited[i]==0:
            visited[i]=1
            cur_lst.append(s_lst[i])
            dfs(k+1)
            cur_lst.pop()
            visited[i]=0

dfs(0)

print(0)