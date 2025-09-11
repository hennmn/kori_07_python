'''
외부 패키지의 설치 # 1 :settings를 통한 방법
좌측 상단 메뉴 버튼(햄버거) -> file -> settings(혹은 alt + ctrl + s)
좌측 리스트에서 project: 프로젝트명으로 되어 있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 # 2
alt + f12 눌러서 터미널 켠다
pip install prettytable
'''
from prettytable import PrettyTable

from ch10_prettytable.pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ["번호", "이름", "타입"]

for add in pokemon_data:
    table.add_row(add)

table.add_rows(pokemon_data)

print(table)

from prettytable import PrettyTable
table = PrettyTable()
exception = [
    (1, 'BaseException', '최상위 예외 클래스'),
    (2, 'Exception', '대부분 예외 클래스의 슈퍼 클래스'),
    (3, 'ArithmeticError', '산술 연산에 문제가 있을 때'),
    (4, 'AttributeError', '잘못된 속성을 참조할 때'),
    (5, 'E0FError', '파일에서 더 이상 읽어 들일 데이터가 없을 때'),
    (6, 'ModulNotFoundError', 'import할 모듈이 없을 때'),
    (7, 'FileNotFoundError', '존재하지 않는 파일일 때'),
    (8, 'IndexError', '잘못된 인덱스를 사용할 때'),
    (9, 'NameError', '잘못된 이름(변수)을 사용할 때'),
    (10, 'SyntaxError', '문법이 틀렸을 때'),
    (11, 'TypeError', '계산하려는 데이터의 유형이 잘못되었을 때'),
    (12, 'ValueError', '계산하려는 데이터의 값이 잘못되었을 때')
]
table.field_names = ["순번", "예외 클래스", "의미"]
table.add_rows(exception)
print(table)

