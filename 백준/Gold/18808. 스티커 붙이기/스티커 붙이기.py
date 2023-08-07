def rotate_90(arr):
    r=len(arr)
    c=len(arr[0])
    new_arr=[[0]*r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_arr[j][r-1-i]=arr[i][j]
    return new_arr

#현재 arr에 스티커를 붙일 수 있는지 없는지 확인해서 좌표 반환
def check_ok(s_arr):
    r=len(s_arr)
    c=len(s_arr[0])
    for i in range(n-r+1):
        for j in range(m-c+1):
            isok=True
            for x in range(i,i+r):
                for y in range(j,j+c):
                    if arr[x][y]==1 and s_arr[x-i][y-j]==1:
                        isok=False
                        break
                if not isok:
                    break
            if isok:
                return i,j
    return -1,-1





def put_sticker(s_arr):
    global arr
    for _ in range(4):
        sx,sy=check_ok(s_arr)
        #스티커 붙이기 가능
        if sx!=-1:
            r=len(s_arr)
            c=len(s_arr[0])
            for i in range(r):
                for j in range(c):
                    if s_arr[i][j]==1:
                        arr[sx+i][sy+j]=1
            break
        else:
            s_arr=rotate_90(s_arr)




def print_arr(arr):
    for lst in arr:
        for n in lst:
            print(n,end=" ")
        print()
    print()

n,m,k=map(int,input().split())

arr=[[0]*m for _ in range(n)]

for _ in range(k):
    s_arr=[]
    r,c=map(int,input().split())
    for i in range(r):
        s_arr.append(list(map(int,input().split())))
    put_sticker(s_arr)
result=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            result+=1
print(result)