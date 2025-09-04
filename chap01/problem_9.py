# 9. 두 개의 3x3 행렬을 입력받아 행렬덧셈 결과행렬을 반환하는 함수

def create_matrix():
    matrix = []
    print("3x3 행렬을 입력하세요:")
    
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"행 {i+1}, 열 {j+1}의 값: "))
            row.append(value)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix, name="행렬"):
    print(f"{name}:")
    for row in matrix:
        print(" ".join(f"{val:4}" for val in row))
    print()

def add_matrices(matrix1, matrix2):
    result = []
    
    for i in range(3):
        row = []
        for j in range(3):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

print("첫 번째 3x3 행렬 입력:")
matrix1 = create_matrix()
print_matrix(matrix1, "첫 번째 행렬")

print("두 번째 3x3 행렬 입력:")
matrix2 = create_matrix()
print_matrix(matrix2, "두 번째 행렬")

result_matrix = add_matrices(matrix1, matrix2)
print_matrix(result_matrix, "덧셈 결과 행렬")

print("행렬 덧셈이 완료되었습니다!")
