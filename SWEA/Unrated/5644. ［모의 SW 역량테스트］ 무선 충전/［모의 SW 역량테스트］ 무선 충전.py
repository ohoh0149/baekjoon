


def get_score():
    #ax ay  bx by
    #a부터 접속 가능 bclst 찾기
    a_bc_lst=[]
    b_bc_lst=[]
    for idx,bc in enumerate(bc_lst[1:],start=1):
        #print(idx)
        if abs(bc[0]-ax)+abs(bc[1]-ay)<=bc[2]:
            a_bc_lst.append(idx)
        if abs(bc[0] - bx) + abs(bc[1] - by) <= bc[2]:
            b_bc_lst.append(idx)
    #print(a_bc_lst)
    #print(b_bc_lst)
    a_bc=0
    b_bc=0
    if len(a_bc_lst)!=0:
        a_bc=a_bc_lst[0]
    if len(b_bc_lst)!=0:
        b_bc=b_bc_lst[0]
    a_score=0
    b_score=0
    #둘다 충전 불가한 경우
    if a_bc==0 and b_bc==0:
        pass
    #겹치지 않는 경우
    elif a_bc!=b_bc:
        a_score=bc_lst[a_bc][3]
        b_score=bc_lst[b_bc][3]
    #겹치는 경우
    else:
        #둘다 하나만 가능하고 겹치는 경우
        if len(a_bc_lst)==1 and len(b_bc_lst)==1:
            a_score=bc_lst[a_bc][3]//2
            b_score=a_score
        else:
            #a가능 길이 1 일때
            if len(a_bc_lst)==1:
                a_score=bc_lst[a_bc][3]
                b_score=bc_lst[b_bc_lst[1]][3]
            #b가능 길이 1일때
            elif len(b_bc_lst)==1:
                b_score=bc_lst[b_bc][3]
                a_score=bc_lst[a_bc_lst[1]][3]
            #둘다 길이가 2이상 이므로 둘중 큰거랑 최고인거랑
            else:
                a_score=bc_lst[a_bc][3]
                b_score=max(bc_lst[a_bc_lst[1]][3],bc_lst[b_bc_lst[1]][3])
    return a_score+b_score


T = int(input())

dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    #총 이동시간 , bc의 개수
    m,a=map(int,input().split())
    a_move_lst=list(map(int,input().split()))
    b_move_lst=list(map(int,input().split()))
    bc_lst=[]
    for _ in range(a):
        bc_lst.append(list(map(int,input().split())))
    bc_lst.sort(key=lambda x:x[3], reverse=True)
    bc_lst.insert(0,[-1,-1,-1,0])
    ax,ay=1,1
    bx,by=10,10
    result=0

    for turn in range(m+1):
        #체크하고 이동
        score=get_score()
        #print(score)
        result+=score


        if turn ==m:
            break

        ax=ax+dx[a_move_lst[turn]]
        ay=ay+dy[a_move_lst[turn]]
        bx=bx+dx[b_move_lst[turn]]
        by=by+dy[b_move_lst[turn]]

    print("#"+str(test_case),result)




    # ///////////////////////////////////////////////////////////////////////////////////
