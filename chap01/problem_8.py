# 8. 두 개의 자연수를 입력받아 그 두 수 사이의 홀수만을 더해서 반환하는 함수 (단, 그 두 수도 포함)

def sum_odd_numbers_between(n, m):
    if n > m:
        n, m = m, n
    
    odd_numbers = []
    for i in range(n, m + 1):
        if i % 2 == 1:
            odd_numbers.append(i)
    
    total = sum(odd_numbers)
    
    print(f"{n}부터 {m}까지의 범위")
    print(f"홀수들: {odd_numbers}")
    print(f"홀수 합계: {' + '.join(map(str, odd_numbers))} = {total}")
    
    return total

# 사용자 입력
n = int(input("첫 번째 자연수: "))
m = int(input("두 번째 자연수: "))

if n <= 0 or m <= 0:
    print("자연수(양의 정수)를 입력해주세요.")
else:
    result = sum_odd_numbers_between(n, m)
    print(f"최종 결과: {result}")
