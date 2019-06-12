# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
import sys

while 1:
    number = input('수를 입력하세요: ')
    try :
        number = int(number)
        if number == 0 :
            sys.exit(0)
        if number %2 == 0:
            print('짝수')
        else :
            print('홀수')
    except  ValueError:
        print('정수가 아닙니다')
    print('\nProcess finished with exit code 0\n')
