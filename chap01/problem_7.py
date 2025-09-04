# 7. 문자열과 하나의 문자를 받아 문자열에서 그 문자가 위치를 모두 찾아 콘솔에 출력하고 그 갯수를 반환하는 함수 (예: Hello, l -> 2,3 출력하고 2를 반환)

def find_character_positions(text, char):
    positions = []
    
    for i, c in enumerate(text):
        if c == char:
            positions.append(i)
    
    print(f"문자열: '{text}'")
    print(f"찾을 문자: '{char}'")
    
    if positions:
        print(f"찾은 위치: {', '.join(map(str, positions))}")
        print(f"총 개수: {len(positions)}")
    else:
        print("해당 문자를 찾을 수 없습니다.")
        print("총 개수: 0")
    
    return len(positions)

# 사용자 입력
text = input("문자열을 입력하세요: ")
char = input("찾을 문자를 입력하세요: ")

if len(char) > 1:
    char = char[0]
    print(f"한 글자만 사용합니다: '{char}'")

result = find_character_positions(text, char)
print(f"반환된 개수: {result}")
