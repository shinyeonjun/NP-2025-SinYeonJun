# 10. 학번이 문자열로 주어지면 입학년도를 정수로 반환하는 함수

def extract_admission_year(student_id):
    if len(student_id) < 4:
        print("학번이 너무 짧습니다.")
        return None
    
    try:
        year = int(student_id[:4])
        
        if 1900 <= year <= 2034:
            print(f"학번: {student_id}")
            print(f"입학년도: {year}년")
            return year
        else:
            print(f"추출된 년도 {year}가 유효하지 않습니다.")
            return None
            
    except ValueError:
        print("학번의 앞 4자리가 숫자가 아닙니다.")
        return None

# 테스트 케이스들
test_cases = [
    "2023123456",  # 2023년 입학
    "2019876543",  # 2019년 입학
    "2025000001",  # 2025년 입학
    "1999123456",  # 1999년 입학
    "abc123456",   # 잘못된 형식
    "123",         # 너무 짧음
]

print("=== 학번에서 입학년도 추출 테스트 ===")
for student_id in test_cases:
    print(f"\n테스트 케이스: {student_id}")
    result = extract_admission_year(student_id)
    if result:
        print(f"결과: {result}년")
    else:
        print("결과: 추출 실패")

# 사용자 입력 테스트
print("\n=== 사용자 입력 테스트 ===")
user_input = input("학번을 입력하세요: ")
result = extract_admission_year(user_input)

if result:
    print(f"입학년도: {result}년")
else:
    print("입학년도 추출에 실패했습니다.")
