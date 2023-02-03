from itertools import combinations
n=int(input())
arr=[[0]*(n+1)]
for i in range(n):
    arr.append([0]+list(map(int,input().split())))

#print(arr)
comb=list(combinations(range(1,n+1),n//2))
#print(comb)

team1=[]
team2=[]
result=1e9
for co in comb:
    team1_s=0
    team2_s=0
    team1=[]
    team2=[]
    for i in range(1,n+1):
        if i in co:
            team1.append(i)
        else:
            team2.append(i)
    #print(team1)
    #print(team2)
    team1_comb=list(combinations(team1,2))
    team2_comb=list(combinations(team2,2))
    for a in team1_comb:
        team1_s+=arr[a[0]][a[1]]+arr[a[1]][a[0]]
    for a in team2_comb:
        team2_s+=arr[a[0]][a[1]]+arr[a[1]][a[0]]
    if abs(team1_s-team2_s)<result:
        result=abs(team1_s-team2_s)
print(result)




