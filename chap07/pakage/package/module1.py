# module1.py
# 패키지 내부 모듈 1

class Class1:
    """Class1 예제 클래스"""
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"안녕하세요! {self.name}입니다."
    
    def some_function(self):
        return "Class1의 some_function() 호출됨"

def helper_function():
    """모듈1의 헬퍼 함수"""
    return "module1의 helper_function() 호출됨"
