# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
#
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )


def cal ( num , is_odd) :
    sum_odd = 0
    sum_even = 0
    for i in range (1,num+1) :
        if(i % 2==1 ) :
            sum_odd+=i
        else :
            sum_even+=i
    if is_odd :
        return sum_odd
    else :
        return sum_even

while 1:
    number = input('숫자를 입력하세요: ')
    try :
        number = int(number)
        sum= 0
        if number == 0:
            break
        if number % 2 == 1:
           sum = cal(number,True)
        else:
            sum = cal(number,False)
        print('결과 값 : ',sum)
    except  ValueError:
        print('정수가 아닙니다')