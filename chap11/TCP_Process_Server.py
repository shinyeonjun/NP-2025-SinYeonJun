# 클라이언트로부터 1~10까지의 숫자를 받으면 영어를 전송하는 서버 프로그램
import socket

# 숫자 문자열 → 영어 단어 매핑
table = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine', '10': 'ten'
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                     # 기본으로 AF_INET, SOCK_STREAM 사용
address = ('localhost', 2500)
s.bind(address)
s.listen(1)
print('Waiting...')
c_socket, c_addr = s.accept()
print("Connection from ", c_addr)

while True:
    data = c_socket.recv(1024).decode()
    try:
        resp = table[data]
    except:
        c_socket.send('Try again'.encode())
    else:
        c_socket.send(resp.encode())
        