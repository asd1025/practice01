# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

a= [1,2,3,4,6,9]
def list_cal(list) :
    count =0
    sum = 0
    for i in  list :
        if(i%3==0) :
            count+=1
            sum += i
    print ('주어진 리스트에서 3의 배수의 개수=> ',count)
    print ('주어진 리스트에서 3의 배수의 합=> ',sum)

list_cal(a)