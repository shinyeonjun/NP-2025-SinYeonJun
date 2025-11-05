# TCP 클라이언트 프로그램 - 서버에 연결하여 메시지를 전송하고, 수신 메시지를 출력하는 클라이언트 프로그램
import socket
port = int(input("Port No: "))
address = ("localhost", port)                           # 서버 주소와 포트 번호
BUFSIZE = 24
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)                                      # 서버 연결 요청
while True:
    msg = input("Message to send: ")
    s.send(msg.encode())                                # 메시지 전송
    data = s.recv(BUFSIZE)                              # 메시지 수신
    print("Received message: %s" % data.decode())       # bytes형을 문자열로 변환

    