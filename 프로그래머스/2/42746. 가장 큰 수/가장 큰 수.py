def solution(numbers):
    answer=''
    lst=[]
    for num in numbers:
        lst.append(((str(num)*3),-num))
    lst.sort(reverse=True)
    #print(lst)
    for _,num in lst:
        answer+=str(-num)
    
    answer=str(int(answer))
    return answer


# # def solution(numbers):
# #     answer = ''
# #     count=0
# #     new_lst=[]
# #     #numbers=[3, 30, 34, 5, 9,1000,0,0,1000]	

# #     for num in numbers:
# #         if 0<=num<10:
# #             new_lst.append(int(str(num)*3)+0.1)
# #         elif num<100:
# #             ten=str(num)[0]
# #             one=str(num)[1]
# #             if ten>one:
# #                 new_lst.append(int(ten+one+ten)-0.1)
# #             elif ten<one:
# #                 new_lst.append(int(ten+one+one)-0.1)
# #             else:
# #                 new_lst.append(int(ten*3)+0.9)
# #         elif num<1000:
# #             new_lst.append(num)
# #         else:
# #             new_lst.append(0.3)
# #     #print(new_lst)

# #     new_lst.sort(reverse=True)
# #     #print(new_lst)
# #     result=""
# #     for num in new_lst:
# #         a=str(num)
# #         if a[-2:]==".1":
# #             result=result+a[0]
# #         elif a[-2:]==".2":
# #             result=result+a[0:2]
# #         elif a[-2:]==".9":
# #             result=result+a[0:2]
# #         elif a[-2:]==".3":
# #             result=result+"1000"
# #         else:
# #             result=result+a
# #         #print(result)

# #     answer=str(int(result))
# #     return answer