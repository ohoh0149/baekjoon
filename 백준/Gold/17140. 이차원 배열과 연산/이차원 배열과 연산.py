import sys
input=sys.stdin.readline
r,c,k=map(int,input().split())

arr=[]
for i in range(3):
    arr.append(list(map(int,input().split())))


def r_operation(arr):
    return_arr=[]
    max_row_count=0
    for row in arr:
        count_row=[0]*101
        for i in row:
            count_row[i]+=1
        #print(count_row)
        temp_arr=[]
        for i in range(1,101):
            if count_row[i]!=0:
                temp_arr.append([i,count_row[i]])
        temp_arr.sort(key=lambda x:x[1])
        tmp=[]
        tmp_count=0
        for i in range(len(temp_arr)):
            tmp.append(temp_arr[i][0])
            tmp.append(temp_arr[i][1])
            tmp_count+=2
            if tmp_count==100:
                break
        max_row_count=max(max_row_count,tmp_count)
        return_arr.append(tmp)
    #print(max_row_count)
    for row in return_arr:
        while len(row)<max_row_count:
            row.append(0)
    #print(return_arr)
    return return_arr
    

        
#r_operation(arr)
def arr_transpose(arr):
    return_arr=[[0]*len(arr) for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            return_arr[j][i]=arr[i][j]
    return return_arr

#print(arr_transpose(arr))

def c_operation(arr):
    array=arr_transpose(arr)
    ar=r_operation(array)
    return arr_transpose(ar)
    
    return 0
#print(c_operation(arr))

result=-1
for i in range(0,101):
    if r-1>=len(arr) or c-1>=len(arr[0]):
        pass
    elif arr[r-1][c-1]==k:
        result=i
        break
    if len(arr)>=len(arr[0]):
        arr=r_operation(arr)
    else:
        arr=c_operation(arr)
   # print(arr)

print(result)