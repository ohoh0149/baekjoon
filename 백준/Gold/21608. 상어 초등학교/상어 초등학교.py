n=int(input())
arr=[]
for i in range(n*n):
    arr.append(list(map(int,input().split())))
###print(arr)

classroom=[[0]*n for i in range(n)]


dx=[-1,0,1,0]
dy=[0,1,0,-1]
def get_like_count(x,y,student_num,like_arr):
    ##print("like_arr",like_arr)
    count=0
    ##print("x y ",x,y)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        ##print("classroom",classroom)
        ##print("nx ny ",nx,ny)
        if 0<=nx<n and 0<=ny<n and classroom[nx][ny] in like_arr:
            count+=1
    return count


def get_max_like_index(num_like_arr):#[student_num, like1,like2,lik3,lik4]
    temp_arr=[[0]*n for i in range(n)]
    return_arr=[]
    student_num=num_like_arr[0]
    like_arr=num_like_arr[1:5]
    max_count=0
    zeroCount=0
    for i in range(n):
        for j in range(n):
            if classroom[i][j]!=0:
                continue
            ##print("i,j",i,j)
            zeroCount+=1
            temp_arr[i][j]=get_like_count(i,j,student_num,like_arr)

            if max_count<=temp_arr[i][j]:
                max_count=temp_arr[i][j]
    if max_count==0:
        for i in range(n):
            for j in range(n):
                if classroom[i][j]==0:
                    return_arr.append((i,j))
        return return_arr
    for i in range(n):
        for j in range(n):
            if temp_arr[i][j]==max_count:
                return_arr.append((i,j))
    ##print(max_count)
    ##print("temp_arr",temp_arr)
    return return_arr

def count_empty(r,c):
    count=0
    for i in range(4):
        nx=r+dx[i]
        ny=c+dy[i]
        if 0<=nx<n and 0<=ny<n and classroom[nx][ny] ==0:
            count+=1
    ###print(r,c,count)
    return count

for num_like_arr in arr:
    ##print("num_like_arr",num_like_arr)
    candidate=get_max_like_index(num_like_arr)
    #print("candidate",candidate)
    if len(candidate)==1:
        classroom[candidate[0][0]][candidate[0][1]]=num_like_arr[0]
      #  print(classroom)
        continue
    if len(candidate)==0:
        continue
    max_count=0
    rx=candidate[0][0]
    ry=candidate[0][1]
    for r,c in candidate:
        if count_empty(r,c)>max_count and classroom[r][c]==0:
            max_count=count_empty(r,c)
            rx=r
            ry=c
            ##print("rx,ry",rx,ry)
    classroom[rx][ry]=num_like_arr[0]
    #print(classroom)

temp_index_arr=[None]*(n*n+1)
result=0
for num_like_arr in arr:
    temp_index_arr[num_like_arr[0]]=(num_like_arr[1:5])
#print("temp_index_arr",temp_index_arr)

for i in range(n):
    for j in range(n):
        temp_count=0
        if classroom[i][j]!=0:
            temp_count+=get_like_count(i,j,classroom[i][j],temp_index_arr[classroom[i][j]])
        if temp_count==0:
            continue
        result+=(10**(temp_count-1))

    
#print(classroom)
print(result)

    


