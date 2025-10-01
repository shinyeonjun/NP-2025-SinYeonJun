# 모듈 사용 예제

# 1. 전체 모듈 import
import myModule

print("=== 전체 모듈 import 예제 ===")
print(f"1부터 10까지의 합: {myModule.sum(10)}")
print(f"2의 5제곱: {myModule.power(2, 5)}")

# 2. 특정 함수만 import
from myModule import sum, power

print("\n=== 특정 함수 import 예제 ===")
print(f"1부터 100까지의 합: {sum(100)}")
print(f"3의 4제곱: {power(3, 4)}")
