# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

a = []
sum = 0
idx = 0
while idx < 5 :
    try:
        number = input('> ')
        number = int (number)
        sum += number
        a.append(number)
        idx += 1
    except  ValueError:
        print('정수가 아닙니다')

print('평균 : ',sum/5)