n = int(input())
data=list(map(int,input().split()))
#print(An)
plusCount,minusCount,mulCount,divCount=map(int,input().split())
#print(plusCount,minusCount,mulCount,divCount)

min_value=1e9
max_value=-1e9

def dfs(i , now):
  global plusCount,minusCount,mulCount,divCount,min_value,max_value
  if i ==n:
    min_value=min(min_value,now)
    max_value=max(max_value,now)
  else:
    if plusCount>0:
      plusCount-=1
      dfs(i+1,now+data[i])
      plusCount+=1
    if minusCount>0:
      minusCount-=1
      dfs(i+1,now-data[i])
      minusCount+=1
    if mulCount>0:
      mulCount-=1
      dfs(i+1,now*data[i])
      mulCount+=1
    if divCount>0:
      divCount-=1
      dfs(i+1,int(now/data[i]))
      divCount+=1

dfs(1,data[0])

print(max_value)
print(min_value)