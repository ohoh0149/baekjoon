
def process():
    for j in range(1,n+1):
        num=j
        for i in range(1,h+1):
            #print(num)
            if arr[i][num]==1:
                num+=1
            elif arr[i][num-1]==1:
                num-=1
        #print(num)
        if num!=j:
            return False
    return True







n,m,h=map(int,input().split())

arr=[[0]*(n+1) for _ in range(h+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
#print(arr)
#process()
#exit()

xy_list=[]
for i in range(1,h+1):
    for j in range(1,n):
        if arr[i][j]==0:
            xy_list.append((i,j))
#print(xy_list)

l=len(xy_list)
result=-1

if process():
    result=0

#choose one
if result==-1:
    for x,y in xy_list:
        arr[x][y]=1
        if process():
            result=1
            break
        arr[x][y]=0

if result==-1:
    for i in range(l):
        for j in range(i+1,l):
            x1,y1=xy_list[i][0],xy_list[i][1]
            x2,y2=xy_list[j][0],xy_list[j][1]
            arr[x1][y1]=1
            arr[x2][y2]=1
            if process():
                result=2
                break
            arr[x1][y1]=0
            arr[x2][y2]=0
if result == -1:
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j+1,l):
                x1, y1 = xy_list[i][0], xy_list[i][1]
                x2, y2 = xy_list[j][0], xy_list[j][1]
                x3,y3=xy_list[k][0],xy_list[k][1]
                arr[x1][y1] = 1
                arr[x2][y2] = 1
                arr[x3][y3]=1
                if process():
                    result=3
                    break
                arr[x1][y1] = 0
                arr[x2][y2] = 0
                arr[x3][y3]=0
print(result)










