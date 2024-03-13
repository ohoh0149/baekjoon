n=int(input())
arr=[list(input()) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx=[0,1]
dy=[1,0]
result=0

def get_result():
    max_count=1
    for i in range(n):
        cur=arr[i][0]
        count=1
        cur2=arr[0][i]
        count2=1
        for j in range(1,n):
            if cur==arr[i][j]:
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
                cur=arr[i][j]

            if cur2==arr[j][i]:
                count2+=1
                max_count=max(count2,max_count)
            else:
                count2=1
                cur2=arr[j][i]

    return max_count



for i in range(n):
    for j in range(n):
        for d in range(2):
            nx=i+dx[d]
            ny=j+dy[d]
            if in_range(nx,ny) and arr[i][j]!=arr[nx][ny]:
                arr[i][j],arr[nx][ny]=arr[nx][ny],arr[i][j]
                result=max(result,get_result())
                arr[nx][ny],arr[i][j]=arr[i][j],arr[nx][ny]

print(result)
