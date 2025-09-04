# 4. 정수 1개를 받아 십진수, 2진수, 8진수, 16진수로 출력하는 함수

def print_in_different_bases(number):
    print(f"입력된 정수: {number}")
    print(f"십진수: {number}")
    print(f"2진수: {bin(number)}")
    print(f"8진수: {oct(number)}")
    print(f"16진수: {hex(number)}")
    
    print(f"2진수 (접두사 없음): {bin(number)[2:]}")
    print(f"8진수 (접두사 없음): {oct(number)[2:]}")
    print(f"16진수 (접두사 없음): {hex(number)[2:].upper()}")

# 사용자 입력
number = int(input("정수를 입력하세요: "))
print_in_different_bases(number)
