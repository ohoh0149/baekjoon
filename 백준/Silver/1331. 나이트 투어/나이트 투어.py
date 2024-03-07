def get_pos(s):
    return int(s[1])-1,ord(s[0])-65,

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
visited=[[0]*6 for _ in range(6)]
r,c=get_pos(input())
sr,sc=r,c
visited[r][c]=1
for _ in range(35):
    nr,nc=get_pos(input())
    if visited[nr][nc]:
        print("Invalid")
        exit()
    ok_flag=False
    for d in range(8):
        if nr==r+dx[d] and nc==c+dy[d]:
            ok_flag=True
            break
    if not ok_flag:
        print("Invalid")
        exit()
    visited[nr][nc]=1
    r,c=nr,nc

ok_flag=False
for d in range(8):
    if sr==r+dx[d] and sc==c+dy[d]:
        ok_flag=True
        break
if ok_flag:
    print("Valid")
else:
    print("Invalid")