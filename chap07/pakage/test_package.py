# 패키지 사용 예제

print("=== 1. 전체 패키지 import ===")
# __init__.py가 실행되면서 "mypackage 패키지가 로드되었습니다." 출력됨
import package

print(f"패키지 버전: {package.__version__}")
print(f"패키지 작성자: {package.__author__}")

print("\n=== 2. 패키지 내 특정 클래스/함수 import ===")
from package import Class1, function2

# Class1 사용
obj1 = Class1("홍길동")
print(obj1.greet())
print(obj1.some_function())

# function2 사용
result = function2(10, 20)
print(f"function2(10, 20) = {result}")

print("\n=== 3. 특정 모듈 전체 import ===")
from package import module1, module2

# module1 사용
helper_result = module1.helper_function()
print(helper_result)

# module2 사용
obj2 = module2.Class2(15)
print(f"Class2 calculate() = {obj2.calculate()}")
print(module2.another_function())

print("\n=== 4. 동적 모듈 로딩 사용 ===")
# __init__.py에 정의된 load_module 함수 사용
loaded_module = package.load_module("module1")
print(f"동적으로 로드된 모듈: {loaded_module}")
