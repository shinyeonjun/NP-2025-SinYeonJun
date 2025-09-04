# 1. "나는 OOO입니다" 형태로 나를 소개하는 함수를 작성하고 호출하여 실행되는 프로그램을 작성하기

def introduce_myself(name):
    print(f"나는 {name}입니다")

# 사용자 입력으로 테스트
user_name = input("당신의 이름을 입력하세요: ")
introduce_myself(user_name)
