#한 번호가 다른 번호의 접두어인지 확인
# 구조대 전화번호는 영석이의 전화번호의 접두사
# 어떤 번호가 다른 번호의 접두어인 경우 -> false
#그렇지 않은 경우 -> true
def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
             
    return answer