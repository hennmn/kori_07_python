class Student:
    # 생성자 정의
    def __init__(self,name,student_id,grades):
        self._name = name
        self._student_id = student_id
        # 성적을 저장하기 위한 빈 딕셔너리 -> 과목명이 key, 점수가 value가 되겠네요.
        self._grades = {}

    # python 버전의 getter에 해당함
    @property
    def name(self):
        return self._name

    #python 버전의 setter의 예시
    @name.setter
    def name(self, value):
        self._name = value


student1 = Student('김일', 2025001, {'국어' : 100})
# getter 의 호출 예시 객체명.속성명 -> 객체명.메서드명() 이 아니라는 것에 주목해야 합니다.
print(f'학생이름 : {student1.name}')

# setter의 호출 예시
student1.name = '김영'
# getter 재호출
print(f'변경된 학생이름 : {student1.name}')

def set_age(self,age):
    if 0 < age <= 100:
        self._age = age

def set_score(self,score):
    if 0.0 <= score <= 4.5:
        self._score = score
    else:
        print('불가능한 나이 입력입니다.')
        return
# 여기에 else return을 굳이 쓸 필요가 없음
# 파이썬 함수는 return이 없으면 자동으로 None을 반환하기 때문에, else: return을 추가해도 동작은 동일.

'''
이상의 코드에서 확인 가능한 것은 Java를 기준으로만 python 코드를 생각할 때 의문스러운 점이 많다는 겁니다.
1. _name이라는 속성이 있는데 객체명.name을 통해서 '김일' / '김영' 이라는 속성값이 출력된다는 점

2. 객체명._name = '김영'이 아니라 객체명.name = '김영'으로 객체의 속성값을 직접 바꾼 것처럼 보인다는 점

이 문제가 되겠습니다.

그런데 이건 Java 기준으로 본 것이고 python으로 풀었을 때눈, 
애초에 _name / name은 서로 다른 개념인데 '_'가 분으면 파이썬 언너 내부적으로 동일한 속성으로 처리해줍니다.

다만 더 신기한 것은 객체명.속성명 뒤에 ()가 없음에도 불구하고 그냥 파이썬은 이걸 메서드처럼 처리해준다는 겁니다.
그래서 '객체명.속성명'이면 getter로 처리해주고, '객체명.속성명 = 데이터'면 setter로 처리해준다고 보시면 됩니다.

이상의 코드라인이 성립하기 위해서 필수적인 부분이
'@property'와 '@속성명.setter' 라는 '데코레이터(decorator)' 때문입니다.

그래서 이거 원래는 자동 생성되기 때문에 일일이 애너테이션 달고 _속성명인지 그냥 속성명인지 따질 필요가 없는데 지금은 좀 쓸모가 없는 상황입니다.

저희는 python으로 백엔드를 짜지 않을 거기 때문에 일단 이런방식으로 setter / getter를 생성한다는 점만 유의해두시고 springboot에 대비하여 Java의 방식의 setter / getter를 작성하겠습니다. 

그렇다면 Java를 기준으로 봤을 때 setter 내부에는 비지니스 로직이 들어갈 수 있었습니다.

완전 동일하게 할겁니다.

set_age() 의 경우에 내부에 로직으로 0살 미만과 200살 초과의 나이는 입력이 불가능하게끔 하겠습니다.

set_score() 의 경우에도 0.0 미만과  4.5초과는 입력이 불가능하게끔 비지니스 로직을 작성하세요.

여기서 생기는 의문점은 그겁니다 -> 아니 매개변수 생성자를 통해서 생성했는데 객체 생성 시점에 -102살 입력하면 되는 거 아니냐 할 수 있는데 추후 설명하겠습니다.
'''
student1.set_age(300)