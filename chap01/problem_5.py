# 5. 두 정수 n부터 m까지 1씩 증가하면서 숫자를 합한 결과를 출력하는 함수 (n과 m 포함)

def sum_range(n, m):
    if n > m:
        n, m = m, n
    
    total = sum(range(n, m + 1))
    numbers = list(range(n, m + 1))
    
    print(f"{n}부터 {m}까지의 숫자: {numbers}")
    print(f"합계: {total}")
    
    return total

# 사용자 입력
n = int(input("시작 정수: "))
m = int(input("끝 정수: "))

result = sum_range(n, m)
print(f"최종 결과: {result}")
