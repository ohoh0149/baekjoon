n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
result=0

def in_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

dx=[-1,0,1,0]
dy=[0,1,0,-1]

#visited2=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # if visited2[i][j]==1:
        #     continue
        one_lst=[(i,j)]
        for d1 in range(4):
            nx=i+dx[d1]
            ny=j+dy[d1]
            if not in_range(nx,ny) or ((nx,ny) in one_lst):
                continue
            two_lst=[(i,j),(nx,ny)]
            for d2 in range(4):
                nx1 = nx + dx[d2]
                ny1 = ny + dy[d2]

                if not in_range(nx1, ny1) or ((nx1,ny1) in two_lst):
                    continue
                three_lst=[(i,j),(nx,ny),(nx1,ny1)]
                for d3 in range(4):
                    nx2 = nx1 + dx[d3]
                    ny2 = ny1 + dy[d3]

                    if not in_range(nx2, ny2) or ((nx2,ny2) in three_lst):
                        continue
                    four_list=[(i,j),(nx,ny),(nx1,ny1),(nx2,ny2)]
                    temp_sum=0
                    for a,b in four_list:
                        temp_sum+=arr[a][b]
                        result=max(result,temp_sum)
#                    print(four_list)

# ㅗ ㅜ
for i in range(n-1):
    for j in range(m-2):
        temp_sum=arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2]
        result=max(temp_sum,result)
        temp_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]
        result=max(temp_sum,result)

# ㅏ ㅓ
for i in range(n-2):
    for j in range(m-1):
        temp_sum = arr[i ][j+1] + arr[i+1][j + 1] + arr[i + 2][j + 1] + arr[i + 1][j]
        result = max(temp_sum, result)
        temp_sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i + 1][j + 1]
        result = max(temp_sum, result)


print(result)

