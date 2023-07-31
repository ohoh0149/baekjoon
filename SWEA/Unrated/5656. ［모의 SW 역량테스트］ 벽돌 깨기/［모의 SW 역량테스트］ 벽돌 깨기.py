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
import copy

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

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def in_range(x,y):
    if 0<=x<h and 0<=y<w:
        return True
    else:
        return False
def bomb(x,y):

    global arr
    global cur_case_result
    num=arr[x][y]
    if num==0:
        return
    else:
        bomb_lst=[]
        arr[x][y]=0
        cur_case_result+=1
        for i in range(1,num):
            for d in range(4):
                nx=x+i*dx[d]
                ny=y+i*dy[d]
                if in_range(nx,ny) and arr[nx][ny]>0:
                    bomb(nx,ny)
                    #bomb_lst.append((nx,ny))
    # for bx,by in bomb_lst:
    #     bomb(bx,by)



def move_down():
    global arr
    new_arr=[[0]*w for _ in range(h)]

    for i in range(w):
        cur_lst=[]
        for j in range(h-1,-1,-1):
            if arr[j][i]>0:
                cur_lst.append(arr[j][i])
        c_idx=0
        #print("cur_lst",i,cur_lst)
        for j in range(h-1,-1,-1):
            if len(cur_lst)==c_idx:
                break
            new_arr[j][i]=cur_lst[c_idx]
            c_idx+=1
    arr=new_arr



def put_ball(case_lst):
    global cur_case_result
    cur_case_result=0
    for i in range(n):
        col=case_lst[i]
        for j in range(h):
            if arr[j][col]>0:
                bomb(j,col)
                move_down()
                break




def dfs(k,lst):
    global result
    global arr
    if k==n:
        copy_arr=copy.deepcopy(arr)
        put_ball(lst)
        result=max(result,cur_case_result)
        arr=copy_arr
        return
    else:
        for i in range(w):
            lst.append(i)
            dfs(k+1,lst)
            lst.pop()




def print_arr(arr):
    for i in range(h):
        print(*arr[i])
    print()
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,w,h=map(int,input().split())
    arr=[]
    for _ in range(h):
        arr.append(list(map(int,input().split())))
    result=0
    cur_case_result=0
    count=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]>0:
                count+=1

    dfs(0,[])
    #print(count,result)
    print("#"+str(test_case),count-result)


    # ///////////////////////////////////////////////////////////////////////////////////
