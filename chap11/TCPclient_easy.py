import socket

# TCP 소켓 생성
sock = socket.create_connection(('localhost',2500 )) # ➊ 소켓 생성과 연결

# 데이터 전송
message ="Client Message"
print ('sending {}'.format (message))
sock.sendall(message.encode())                      # ➋ 데이터를 모두 전송

data =sock.recv(1024)                               # 데이터 수신
print ('received {}'.format (data.decode()))
print ('closing socket')
sock.close()