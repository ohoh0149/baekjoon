def solution(s):
    answer = []
    temp=s.split("},{")

    lst=[]
    if len(temp)==1:
        answer.append(int(temp[0][2:-2]))
    else:
        temp[0]=temp[0][2:]

        temp[-1]=temp[-1][:-2]

        for c in temp:
            a=c.split(",")
            lst.append((len(a),set(a)))
        lst.sort()

        n=len(lst)
        answer.append(int(list(lst[0][1])[0]))
        for idx, se in lst:
            if n==idx:
                break

            #print(lst[idx][1])
            #print(se)
            answer.append(int(list(set(lst[idx][1])-set(se))[0]))
        print(answer)


    return answer