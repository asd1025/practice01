# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.


def reverse (str) :
    result = list(str)
    result.reverse()
    print( '결과> ',"".join(result))

str =(input('입력> '))
reverse(str)