def solution(phone_book):
    s=set()
    for phone in phone_book:
        for l in range(len(phone)-1):
            s.add(phone[:l+1])

    for phone in phone_book:
        if phone in s :
            return False
    return True