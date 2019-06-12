# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys


while 1:
    number = input('수를 입력하세요: ')
    try :
        number = int(number)
        if number == 0:
            sys.exit(0)
        if number % 3 == 0:
            print('3의 배수입니다')
        else:
            print('3의 배수가 아닙니다')
    except  ValueError:
        print('정수가 아닙니다')
    print('\nProcess finished with exit code 0\n')
