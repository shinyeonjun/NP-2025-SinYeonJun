# 3. 두 수 a,b를 입력받아 다음 계산을 하는 함수 
# a+b, a << b, a * b를 계산하여 콘솔에 출력하고 후 그 중 가장 큰 값을 반환

def calculate_and_find_max(a, b):
    addition = a + b
    left_shift = a << b
    multiplication = a * b
    
    print(f"a + b = {a} + {b} = {addition}")
    print(f"a << b = {a} << {b} = {left_shift}")
    print(f"a * b = {a} * {b} = {multiplication}")
    
    max_value = max(addition, left_shift, multiplication)
    print(f"가장 큰 값: {max_value}")
    
    return max_value

# 사용자 입력
a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))

result = calculate_and_find_max(a, b)
print(f"반환된 최대값: {result}")
