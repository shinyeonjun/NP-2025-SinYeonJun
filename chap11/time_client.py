# 타임 서버에 접속하여 시간을 읽어 오는 클라이언트 프로그램
import socket                                             # socket 모듈 불러오기

# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address)                                    
print("현재 시각 : ", sock.recv(1024).decode())            # 수신 바이트를 문자열로 변환하여 출력 

