def sum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total

def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * x
    return prod

if __name__ == '__main__':  # myModule.py를 직접 호출할 때만 실행됨
    print(sum(5))
    print(power(2, 3))

# 모듈을 독립된 프로그램으로 사용할 때만 실행됨
# 모듈의 기능을 테스트하기 위해 사용됨