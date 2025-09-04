# 2. 다음 요구사항에 맞는 변수 선언하기
# 1) 정수 5를 저장하는 변수, 2) 실수 2.14를 저장하는 변수, 3) "Hello"를 저장하는 변수, 
# 4) 숫자의 목록 1,2,3,4를 저장하는 변수, 5) 문자열 목록 "Apple", "Banana", "Cherry", "Durian"을 저장하는 변수, 
# 6) 원주율 3.141592 상수를 저장하는 매크로 변수 혹은 상수형 변수 선언, 
# 7) 자신의 이름, 나이, 전화번호로 초기화된 구조체 변수 선언

# 1) 정수 5를 저장하는 변수
a = 5

# 2) 실수 2.14를 저장하는 변수
b = 2.14

# 3) "Hello"를 저장하는 변수
c = "Hello"

# 4) 숫자의 목록 1,2,3,4를 저장하는 변수
d = [1, 2, 3, 4]

# 5) 문자열 목록 "Apple", "Banana", "Cherry", "Durian"을 저장하는 변수
e = ["Apple", "Banana", "Cherry", "Durian"]

# 6) 원주율 3.141592 상수를 저장하는 상수형 변수 선언
PI = 3.141592

# 7) 자신의 이름, 나이, 전화번호로 초기화된 구조체 변수 선언
class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

my_info = Person("김철수", 25, "010-1234-5678")

# 변수들 출력
print(f"정수: {a}")
print(f"실수: {b}")
print(f"문자열: {c}")
print(f"숫자 목록: {d}")
print(f"과일 목록: {e}")
print(f"원주율: {PI}")
print(f"이름: {my_info.name}, 나이: {my_info.age}, 전화번호: {my_info.phone}")
