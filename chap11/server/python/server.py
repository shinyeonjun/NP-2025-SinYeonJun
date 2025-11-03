# TCP 소켓 통신을 위한 표준 라이브러리
import socket
# 멀티스레딩을 위한 라이브러리 (동시 다중 클라이언트 처리)
import threading
# 타입 힌팅을 위한 Optional 타입
from typing import Optional


class ClientHandler(threading.Thread):
	"""
	각 클라이언트 연결을 처리하는 스레드 클래스
	서버가 새로운 클라이언트 연결을 받을 때마다 이 클래스의 인스턴스를 생성하여 독립적으로 처리
	"""
	def __init__(self, conn: socket.socket, addr: tuple[str, int]):
		"""
		클라이언트 핸들러 초기화
		
		Args:
			conn: 클라이언트와의 TCP 소켓 연결 객체
			addr: 클라이언트의 주소 정보 (IP 주소, 포트 번호) 튜플
		"""
		super().__init__(daemon=True)  # 데몬 스레드로 설정 (메인 프로세스 종료 시 자동 종료)
		self.conn = conn  # 클라이언트와의 소켓 연결 저장
		self.addr = addr  # 클라이언트 주소 정보 저장

	def _readline(self) -> Optional[str]:
		"""
		소켓에서 한 줄씩 읽어오는 헬퍼 메서드
		개행 문자(\n)를 만날 때까지 바이트를 읽어서 문자열로 변환
		
		Returns:
			읽어온 줄 문자열 (개행 문자 제거), 연결 종료 시 None 반환
		"""
		buffer = bytearray()  # 바이트 데이터를 임시 저장할 버퍼
		while True:
			chunk = self.conn.recv(1)  # 소켓에서 1바이트씩 읽기
			if not chunk:  # 연결이 끊어진 경우 (0바이트 수신)
				return None
			buffer.extend(chunk)  # 읽은 바이트를 버퍼에 추가
			if chunk == b"\n":  # 개행 문자를 만나면 줄 읽기 완료
				break
		# 버퍼의 바이트를 UTF-8 문자열로 디코딩하고, \r\n 또는 \n 제거
		return buffer.decode("utf-8", errors="replace").rstrip("\r\n")

	def run(self) -> None:
		"""
		스레드가 시작될 때 실행되는 메인 로직
		N-Echo 프로토콜에 따라 클라이언트 요청을 처리
		
		프로토콜: 첫 번째 줄 = n (반복 횟수), 두 번째 줄 = message (메시지 내용)
		서버 동작: message를 n번 반복하여 클라이언트에게 전송
		"""
		try:
			# 프로토콜: 첫 번째 줄 읽기 (n 값)
			first_line = self._readline()
			# 프로토콜: 두 번째 줄 읽기 (message 내용)
			second_line = self._readline()
			if first_line is None or second_line is None:  # 연결이 끊어진 경우
				return
			try:
				# 첫 번째 줄을 정수로 변환 (n = 반복 횟수)
				n = int(first_line.strip())
			except ValueError:
				# 정수 변환 실패 시 에러 메시지 전송 후 종료
				self.conn.sendall(b"ERR invalid n\n")
				return

			message = second_line  # 두 번째 줄이 메시지 내용
			if n < 0:  # 음수는 허용하지 않음
				# 음수 요청 시 에러 메시지 전송 후 종료
				self.conn.sendall(b"ERR n must be >= 0\n")
				return

			# N-Echo 핵심 로직: message를 n번 반복하여 클라이언트에게 전송
			for _ in range(n):
				# 각 메시지 끝에 개행 문자를 추가하여 전송 (프로토콜 규격)
				self.conn.sendall((message + "\n").encode("utf-8"))
		finally:
			# 예외 발생 여부와 관계없이 소켓 연결 종료 (리소스 정리)
			try:
				self.conn.close()
			except Exception:
				pass  # 종료 중 예외는 무시


class TCPEchoServer:
	"""
	N-Echo TCP 서버의 메인 클래스
	서버 소켓을 생성하고 클라이언트 연결을 수신하여 각 연결을 별도 스레드로 처리
	"""
	def __init__(self, host: str = "0.0.0.0", port: int = 50000):
		"""
		서버 초기화
		
		Args:
			host: 서버가 바인딩할 IP 주소 (0.0.0.0 = 모든 네트워크 인터페이스에서 수신)
			port: 서버가 리스닝할 포트 번호 (기본값: 50000)
		"""
		self.host = host  # 서버 호스트 주소 저장
		self.port = port  # 서버 포트 번호 저장
		self._sock: Optional[socket.socket] = None  # 서버 소켓 객체 (초기값: None)
		self._stop_event = threading.Event()  # 서버 종료 신호를 위한 이벤트 객체

	def start(self) -> None:
		"""
		서버 시작 및 클라이언트 연결 대기
		무한 루프로 클라이언트 연결을 받아들여 각 연결을 별도 스레드로 처리
		"""
		# TCP 소켓 생성 (AF_INET = IPv4, SOCK_STREAM = TCP)
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# SO_REUSEADDR 옵션 설정: TIME_WAIT 상태의 포트도 재사용 가능하게 함
		self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# 서버 소켓을 지정된 호스트와 포트에 바인딩
		self._sock.bind((self.host, self.port))
		# 소켓을 리스닝 모드로 설정 (백로그 큐 크기는 기본값 사용)
		self._sock.listen()
		print(f"N-Echo Server listening on {self.host}:{self.port}")
		try:
			# 종료 신호가 올 때까지 무한 루프
			while not self._stop_event.is_set():
				# 클라이언트 연결 요청 대기 (블로킹 호출)
				conn, addr = self._sock.accept()
				print(f"Accepted connection from {addr}")
				# 새로운 클라이언트 연결을 처리할 핸들러 스레드 생성
				handler = ClientHandler(conn, addr)
				# 핸들러 스레드 시작 (독립적으로 클라이언트 요청 처리)
				handler.start()
		finally:
			# 예외 발생 시에도 서버 정상 종료
			self.stop()

	def stop(self) -> None:
		"""
		서버 종료 및 리소스 정리
		모든 클라이언트 핸들러 스레드는 데몬 스레드이므로 자동 종료됨
		"""
		self._stop_event.set()  # 종료 신호 설정 (무한 루프 탈출)
		if self._sock is not None:  # 소켓이 생성된 경우에만 종료
			try:
				self._sock.close()  # 서버 소켓 닫기
			except Exception:
				pass  # 종료 중 예외는 무시
			self._sock = None  # 소켓 객체 초기화


def main() -> None:
	"""
	프로그램 진입점
	명령줄 인자를 파싱하여 서버를 시작하고 종료 신호(Ctrl+C)를 처리
	"""
	import argparse
	# 명령줄 인자 파서 생성
	parser = argparse.ArgumentParser(description="N-Echo TCP Server (send message n times)")
	# 호스트 주소 인자 (기본값: 0.0.0.0 = 모든 인터페이스)
	parser.add_argument("--host", default="0.0.0.0", help="bind host (default: 0.0.0.0)")
	# 포트 번호 인자 (기본값: 50000)
	parser.add_argument("--port", type=int, default=50000, help="bind port (default: 50000)")
	args = parser.parse_args()  # 명령줄 인자 파싱

	# 서버 인스턴스 생성
	server = TCPEchoServer(args.host, args.port)
	try:
		server.start()  # 서버 시작 (무한 루프)
	except KeyboardInterrupt:
		# Ctrl+C (SIGINT) 신호 수신 시
		print("\nShutting down...")
	finally:
		# 예외 발생 여부와 관계없이 서버 종료 및 리소스 정리
		server.stop()


if __name__ == "__main__":
	# 스크립트가 직접 실행될 때만 main() 함수 호출
	main()


