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
#import sys
#sys.stdin = open("input.txt", "r")

def simulate(where_lst):
    #[0,0,0,1,1,1]
    stair_length_lst=[0]*people_len
    #각각 사람들에 대해서 계단까지의 위치 구하기
    for i in range(people_len):
        stair_length_lst[i]=abs(people_xy_lst[i][0]-stair[where_lst[i]][0])+abs(people_xy_lst[i][1]-stair[where_lst[i]][1])
    #print(stair_length_lst)
    cur_stair_lst=[[],[]]
    count=0
    cur_result=0
    for turn in range(50):
        # if where_lst==[0,0,0]:
        #     #print(turn,cur_stair_lst)
        if turn >=result:
            return result
        if count==people_len:
            # if turn-1==10:
            #     print(where_lst)
            #     print(stair_length_lst)
            return turn


        # 계단 두개에 대해서 먼저 내려 가자
        for stair_num in range(2):
            #먼저 0 제거 하자.
            new_lst=[]
            for temp in cur_stair_lst[stair_num]:
                if temp!=0:
                    new_lst.append(temp)
                else:
                    count+=1
            cur_stair_lst[stair_num]=new_lst
            #이제 한칸씩 내려가자 다만 최대 3명만
            l=min(3,len(cur_stair_lst[stair_num]))
            next_lst=[]
            for i in range(l):
                cur_stair_lst[stair_num][i]-=1




        #현재 턴에 계단으로 가야하는 사람 계단에 넣어주기
        for idx,t in enumerate(stair_length_lst):
            if t==turn+1:
                #현재 사람 몇번계단으로 가는지
                w=where_lst[idx]
                cur_stair_lst[w].append(stair[w][2])


    print("this is error!!!")
    return cur_result




def dfs(k,lst):
    global result
    if k==people_len:
        result=min(simulate(lst),result)
        return

    for i in range(2):
        lst.append(i)
        dfs(k+1,lst)
        lst.pop()








T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    people_xy_lst=[]
    stair=[]
    result=1e9
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                continue
            elif arr[i][j]==1:
                people_xy_lst.append((i,j))
            else:
                stair.append((i,j,arr[i][j]))
    #print(people_xy_lst)
    people_len=len(people_xy_lst)
    #print(stair)
    dfs(0,[])

    print("#"+str(test_case),result)
    #print(simulate([0,0,0,0,1,1]))


    # ///////////////////////////////////////////////////////////////////////////////////
