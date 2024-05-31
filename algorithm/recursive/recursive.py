# 일반적인 형태
# def function(입력):
#     if 일정값 < 입력:
#         return function(입력 - 1)
#     else:
#         return 일정값, 입력값, 특정값
#
# def function(입력):
#     if 입력 < 일정값:
#         return 일정값, 입력값, 특정값
#
#     function(입력보다 작은 값)
#     return 결과값

# 회문 (순서를 거꾸로 읽어도 같은 문장) 을 판별하는 함수 작성하기
def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
