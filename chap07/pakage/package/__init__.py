# __init__.py
## 패키지 이름 : mypackage
## 패키지 초기화 및 메타데이터 설정
__version__ = "1.0.0"
__author__ = "Your Name"
## __init__.py 위치
'''
mypackage/
│
├── __init__.py # 패키지 초기화 파일
├── module1.py
└── module2.py
'''
## 패키지 내 주요 클래스 및 함수 노출
from .module1 import Class1
from .module2 import function2
print("mypackage 패키지가 로드되었습니다.")

# 외부에서 다음과 같이 사용:
from mypackage import Class1, function2

## 동적 모듈 로딩
import importlib

def load_module(name):
    return importlib.import_module(f".{name}", package=__name__)
 