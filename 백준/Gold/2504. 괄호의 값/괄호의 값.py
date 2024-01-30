s=input()
#
# a1=0
# a2=0
# isOk=True
# for c in s:
#     if c=="(":
#         a1+=1
#     elif c=="[":
#         a2+=1
#     elif c==")":
#         if a1==0:
#             isOk=False
#             break
#         a1-=1
#     elif c=="]":
#         if a2==0:
#             isOk=False
#             break
#         a2-=1
# if not (a1==0 and a2==0):
#     isOk=False
#
# if isOk:
#     pass
# else:
#     print(0)
#
#
#
stack=[]
isOk=True
for c in s:
    #print(stack)
    if not isOk:
        break
    if c=="(" or c=="[":
        stack.append(c)
    elif c==")":
        temp_num=0
        while stack:
            temp_c=stack.pop()
            if temp_c=="(":
                if temp_num==0:
                    stack.append(2)
                else:
                    stack.append(temp_num*2)
                break
            elif temp_c =="[":
                isOk=False
                break
            #숫자인 경우
            else:
                temp_num+=temp_c
        if not stack:
            isOk=False


    elif c=="]":
        temp_num = 0
        while stack:
            temp_c = stack.pop()
            if temp_c == "[":
                if temp_num == 0:
                    stack.append(3)
                else:
                    stack.append(temp_num * 3)
                break
            elif temp_c == "(":
                isOk = False
                break
            # 숫자인 경우
            else:
                temp_num += temp_c
        if not stack:
            isOk=False


if "(" in stack or "[" in stack:
    isOk=False
if isOk:
    print(sum(stack))
else:
    print(0)