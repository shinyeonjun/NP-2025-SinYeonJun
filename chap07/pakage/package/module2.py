# module2.py
# 패키지 내부 모듈 2

def function2(x, y):
    """두 수를 더하는 함수"""
    return x + y

class Class2:
    """Class2 예제 클래스"""
    def __init__(self, value):
        self.value = value
    
    def calculate(self):
        return self.value * 2

def another_function():
    """모듈2의 다른 함수"""
    return "module2의 another_function() 호출됨"
