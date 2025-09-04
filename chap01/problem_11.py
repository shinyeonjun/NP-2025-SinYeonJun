# 11. 이름, 나이, 전화번호로 구성된 연락처를 반복적으로 입력받아 저장하고 만약 이름이나 나이를 0을 입력하면 입력을 중단하고 
# 입력받은 목록을 반환하는 함수와 입력 받은 연락처 목록을 받아 콘솔에 출력하는 함수 작성한 후 
# 입력받아 출력하는 테스트 코드 작성

class Contact:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}, 전화번호: {self.phone}"

def input_contacts():
    contacts = []
    print("연락처 정보를 입력하세요. (이름이나 나이에 0을 입력하면 중단)")
    
    while True:
        print(f"\n--- {len(contacts) + 1}번째 연락처 ---")
        
        name = input("이름: ").strip()
        if name == "0":
            print("입력을 중단합니다.")
            break
        
        try:
            age = int(input("나이: "))
            if age == 0:
                print("입력을 중단합니다.")
                break
            if age < 0:
                print("나이는 양수여야 합니다. 다시 입력해주세요.")
                continue
        except ValueError:
            print("올바른 나이를 입력해주세요.")
            continue
        
        phone = input("전화번호: ").strip()
        
        contact = Contact(name, age, phone)
        contacts.append(contact)
        print(f"'{name}' 연락처가 추가되었습니다.")
    
    print(f"\n총 {len(contacts)}개의 연락처가 입력되었습니다.")
    return contacts

def print_contacts(contacts):
    if not contacts:
        print("출력할 연락처가 없습니다.")
        return
    
    print(f"\n=== 연락처 목록 (총 {len(contacts)}개) ===")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")
    print("=" * 50)

print("=== 연락처 관리 시스템 ===")

# 1. 연락처 입력받기
print("\n1단계: 연락처 정보 입력")
contact_list = input_contacts()

# 2. 입력받은 연락처 출력하기
print("\n2단계: 입력받은 연락처 출력")
print_contacts(contact_list)

# 3. 추가 테스트: 빈 리스트 출력 테스트
print("\n3단계: 빈 리스트 출력 테스트")
print_contacts([])

print("\n프로그램이 완료되었습니다.")
