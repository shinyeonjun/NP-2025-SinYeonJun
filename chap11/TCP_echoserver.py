# TCP 에코 서버 프로그램 - 수신 데이터를 출력하고 다시 상대방에게 전송
from socket import *                            

port = 2500                                     # 포트 번호
BUFSIZE = 1024                                  # 최대 수신 바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', port))                  
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()  
print('connected by', remotehost, remoteport)   
while True:
    data = conn.recv(BUFSIZE)                   # 데이터 수신
    if not data:                                # data=''이면 종료. ''는 False임
        break                                   
    print("Received message: ", data.decode())  # 수신 데이터 출력. 바이트형으로 수신되므로 문자열로 변환
    conn.send(data)                             # 수신 데이터를 그대로 다시 클라이언트에게 전송
conn.close()                                    # 소켓을 닫음

