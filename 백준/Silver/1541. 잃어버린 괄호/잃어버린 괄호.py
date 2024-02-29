inp=input()
lst=list(inp)

cur=0
flag=False
while True:
    if cur==len(lst):
        if flag:
            lst.append(")")
        break
    if lst[cur]=="0":
        if cur==0 or lst[cur-1] in ["+","-","(",")"]:
            del lst[cur]
            continue
    if lst[cur]=="-":
        if not flag:
            lst.insert(cur + 1, "(")
            flag=True
        else:
            lst.insert(cur,")")
            flag=False
    cur+=1

a="".join(lst)
print(eval(a))