# 6. 하나의 십진수 정수가 주어지면 각 자리의 십진수의 합을 반환하는 함수를 작성 (예: 274 입력 --> 2+7+4 = 13 반환)

def sum_of_digits(number):
    if number < 0:
        number = abs(number)
    
    digits = [int(digit) for digit in str(number)]
    total = sum(digits)
    
    print(f"입력된 정수: {number}")
    print(f"각 자릿수: {digits}")
    print(f"자릿수 합계: {' + '.join(map(str, digits))} = {total}")
    
    return total

# 사용자 입력
number = int(input("정수를 입력하세요: "))
result = sum_of_digits(number)
print(f"최종 결과: {result}")
