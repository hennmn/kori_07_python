'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건문이 False가 될 때까지)]
형식 :
while 조건식1:
    반복실행문

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해두셔야 합니다.
'''
n1 = 1
while n1 < 11:
    print(n1)
    n1 += 1

print()
'''
기본예제
10부터 1까지 역순으로 출력하시오.
'''
n2 = 10
while n2 > 0:
    print(n2)
    n2 -= 1

'''
중첩 while 문(while문 뿐만 아니라 내부에 if를 쓸 수도 있겠습니다.)
중첩 while 및 f-string을 활용하여

구구단 메서드 출력하겠습니다. (while문 사용할 것)
변수명은 dan / number로 하겠습니다.
'''
dan = 2

while dan < 10:     # while은 전연이라 자바때와 달리 밑에서 number을 뽑아낼 수 있음
    number = 1      # 내부에서 선언하면 항상 1로 초기화 할 필요가 없어짐 대박사건
    while number < 10:
        print(f'{dan} x {number} = {dan * number}')
        number += 1
    dan += 1
    print()

print(number)







