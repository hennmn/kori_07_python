# phonenumber = input('전화번호를 입력하시오 >>> ')
# if len(phonenumber) != 13:
#     print('유효하지 않은 전화번호 형식입니다.')
# else:
#     middle = phonenumber[4:8]
# print(f'전화번호의 중간 4자리는 {middle}입니다.')
'''
학생의 이름과 학번, 그리고 과목별 성적을 관리하는 Student 클래스를 작성하시오.

이 클래스는 생성자를 통해 학생 정보와 성적 딕셔너리를 초기화하고, 성적을 추가하는 메서드와 평균 성적을 계산하여 반환하는 메서드를 포함해야 한다.

지시사항:

1. Student 클래스를 정의하고, 생성자(__init__)를 통해 name과 student_id를 초기화하시오. 성적을 저장할 빈 딕셔너리(grades)도 초기화하시오.
참고 -

self.name = name

self.student_id = student_id

self.grade = {}



2. add_grade라는 메서드를 정의하여 subject와 score를 매개변수로 받아 grades 딕셔너리에 추가하시오.

3. get_average_grade라는 메서드를 정의하여 grades 딕셔너리의 점수들을 기반으로 평균 성적을 계산하여 반환하시오.

4. Student 객체를 생성하고, 성적을 추가한 뒤, 평균 성적을 출력하시오.

실행 예:

학생 이름: 김일

평균 성적: 90.0점
'''
# class Student:
#     def __init__(self,name,student_id,grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = {}
#
#     def add_grade(self, subject, score):
#         self.grade[subject] = score
#
#     def get_average_grade(self):
#         values_sum = sum(list(self.grade.values()))
#         avg = values_sum / len(self.grade)
#         print(f'학생 이름 : {self.name} \n평균 성적 : {avg}')
#
#
# student = Student('김일',10, {'국어': 90})
# student.add_grade('수학',100)
# student.add_grade('과학',80)
#
# student.get_average_grade()

'''
사용자로부터 여러 개의 숫자를 입력 받아 리스트에 저장한 후, 해당 리스트에 포함된 숫자들 중 양수, 음수, 0의 개수를 각각 세어 출력하는 프로그램을 작성하시오.

지시사항:

1. 몇 개의 숫자를 입력할지 사용자로부터 입력 받으시오.
2. 입력받은 숫자들을 저장할 빈 리스트(numbers)를 생성하시오.

3. 양수, 음수, 0의 개수를 저장할 변수 3개를 0으로 초기화하시오.

4. for 반복문을 사용하여 입력 받은 횟수만큼 숫자들을 입력 받아 numbers 리스트에 추가하고, 동시에 각 숫자를 판별하여 해당 변수의 값을 1씩 증가 시키시오.

최종적으로 각 변수에 저장된 개수를 출력하시오.

실행 예:

몇 개의 숫자를 입력하시겠습니까? >>> 5

1번째 숫자를 입력하시오 >>> 10

2번째 숫자를 입력하시오 >>> -5

3번째 숫자를 입력하시오 >>> 0

4번째 숫자를 입력하시오 >>> 20

5번째 숫자를 입력하시오 >>> -15

양수: 2개

음수: 2개

0: 1개
'''
# numbers = []
# zero_count = 0
# positive_count = 0
# negative_count = 0
# input_num = int(input('몇 개의 숫자를 입력하시겠습니까? >>> '))
# for i in range(input_num):
#     num = input(f'{i+1}번째 숫자를 입력하시오 >>> ')
#     numbers.append(num)
#     if num == '0':
#         zero_count += 1
#     elif int(num) > 0 :
#         positive_count += 1
#     else:
#         negative_count += 1
# print(f'양수: {positive_count}개 \n음수: {negative_count}개 \n0: {zero_count}개')
'''
다음 예시와 같이, 여러 후보자에 대한 투표 결과를 집계하는 프로그램을 작성하시오. 사용자는 먼저 후보자의 수를 입력하고, 그에 맞춰 후보자들의 이름을 입력한다. 이후 투표 횟수와 각 투표 결과를 숫자로 입력받아 최종 결과를 딕셔너리에 저장하여 출력하시오.

지시사항:

1. 전체 후보자의 수를 사용자로부터 입력받으시오.
2. for 반복문을 사용하여 후보자 수만큼 후보자들의 이름을 입력받고, candidates 리스트에 저장하시오.

3. 각 후보자의 투표 수를 저장할 딕셔너리(votes)를 생성하고, candidates 리스트의 이름을 키로, 초기 투표 수(0)를 값으로 설정하시오.

4. 전체 투표 횟수를 입력받으시오.

5. for 반복문을 사용하여 투표 횟수만큼 사용자로부터 각 투표 결과를 입력받으시오. 입력은 후보자의 순서 번호(1, 2, 3...)로 받으시오.

6. 입력받은 투표 결과에 따라 해당 후보자의 투표 수를 1씩 증가시키시오.

7. 최종적으로 딕셔너리에 저장된 각 후보자의 투표 수를 출력하시오.

실행 예:

후보자 수를 입력하시오 >>> 3

1번째 후보자의 이름을 입력하시오 >>> 김일

2번째 후보자의 이름을 입력하시오 >>> 김이

3번째 후보자의 이름을 입력하시오 >>> 김삼

전체 투표 횟수를 입력하시오 >>> 5

1번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

2번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 2

3번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

4번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 3

5번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

--- 투표 결과 ---

김일: 3표

김이: 1표

김삼: 1표
'''

# candidates = []
# votes = {}
# candidate_num = int(input('후보자 수를 입력하시오 >>> '))
# for i in range(candidate_num):
#     candidates.append(input(f'{i+1}번째 후보자의 이름을 입력하시오 >>> '))
#     votes[candidates[i]] = 0
#
# vote_num = input('전체 투표 횟수를 입력하시오 >>> ')
# for i in range(int(vote_num)):
#     vote_count = input(f'{i+1}번째 투표 (1: {candidates[0]}, 2: {candidates[1]}, 3: {candidates[2]}) >>> ')
#     if vote_count == '1':
#         votes[candidates[0]] += 1
#     elif vote_count == '2':
#         votes[candidates[1]] += 1
#     else:
#         votes[candidates[2]] += 1
#
# print('---투표결과---')
# for name in votes:
#     print(f'{name}: {votes[name]}표')

'''

'''
num = 5524
num_float = float(num)
print(num_float)

str_example = 'hello, python!'
print(str_example[7:13])

print(str_example.upper())

MENU = {
    '에스프레소' : {
        '재료':{
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료':{
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료':{
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.5,
    },
}

print(type(MENU.keys()))