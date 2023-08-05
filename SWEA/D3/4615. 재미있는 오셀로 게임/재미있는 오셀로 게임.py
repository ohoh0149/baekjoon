# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
def in_range(x,y):
    return 1<=x<=n and 1<=y<=n

def check(x,y,d,want):
    while True:
        if not in_range(x,y) or arr[x][y]==0:
            return False
        if arr[x][y]==want:
            return True
        else:
            x=x+dx[d]
            y=y+dy[d]





def put_mal(y,x,t):
    global arr
    rt=[0,2,1]

    arr[x][y]=t
    for d in range(8):
        nx=x+dx[d]
        ny=y+dy[d]
        nx2=nx+dx[d]
        ny2=ny+dy[d]
        if not in_range(nx,ny) or not in_range(nx2,ny2) or arr[nx][ny]!=rt[t]:
            continue
        if check(nx2,ny2,d,t):
            while True:
                if arr[nx][ny]==t:
                    break
                arr[nx][ny]=t
                nx=nx+dx[d]
                ny=ny+dy[d]




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m=map(int,input().split())

    arr=[[0]*(n+1) for _ in range(n+1)]
    arr[n//2][n//2]=2
    arr[n//2+1][n//2+1]=2
    arr[n//2+1][n//2]=1
    arr[n//2][n//2+1]=1
    #for i in range(1,n+1):
        #print(*arr[i][1:])

    for _ in range(m):
        j,i,t=map(int,input().split())
        put_mal(j,i,t)
        # print("put",j,i,t)
        # for x in range(1,n+1):
        #     print(*arr[x][1:])
        # print()


    one_count=0
    two_count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]==1:
                one_count+=1
            elif arr[i][j]==2:
                two_count+=1
    print("#"+str(test_case),one_count,two_count)




    # ///////////////////////////////////////////////////////////////////////////////////
