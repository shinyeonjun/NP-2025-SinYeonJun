# TCP 소켓 통신을 위한 표준 라이브러리
import socket
# 타입 힌팅을 위한 List 타입
from typing import List


class NEchoClient:
	"""
	N-Echo TCP 클라이언트 클래스
	서버에 연결하여 메시지를 n번 반복 수신하는 기능을 제공
	"""
	def __init__(self, host: str, port: int):
		"""
		클라이언트 초기화
		
		Args:
			host: 서버의 IP 주소 또는 호스트명
			port: 서버의 포트 번호
		"""
		self.host = host  # 서버 호스트 주소 저장
		self.port = port  # 서버 포트 번호 저장

	def request(self, n: int, message: str) -> List[str]:
		"""
		N-Echo 프로토콜에 따라 서버에 요청을 보내고 응답을 받아옴
		
		프로토콜:
		1. 서버에 연결
		2. 첫 번째 줄에 n (반복 횟수), 두 번째 줄에 message (메시지) 전송
		3. 서버로부터 message를 n번 받아서 리스트로 반환
		
		Args:
			n: 메시지를 반복 수신할 횟수 (0 이상의 정수)
			message: 서버에 보낼 메시지 내용
		
		Returns:
			서버로부터 받은 메시지들을 담은 문자열 리스트 (n개)
		
		Raises:
			ValueError: n이 음수인 경우
		"""
		if n < 0:  # 음수는 허용하지 않음
			raise ValueError("n must be >= 0")
		
		# 소켓 컨텍스트 매니저 사용 (자동으로 연결 종료 보장)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			# 서버에 TCP 연결 시도 (블로킹 호출)
			sock.connect((self.host, self.port))
			# 프로토콜 형식으로 요청 데이터 생성: "n\nmessage\n"
			payload = f"{n}\n{message}\n".encode("utf-8")
			# 요청 데이터를 서버에 전송 (전체 데이터가 전송될 때까지 보장)
			sock.sendall(payload)
			
			# 서버로부터 받은 응답을 저장할 리스트
			received: List[str] = []
			# 수신한 바이트 데이터를 임시 저장할 버퍼
			buffer = bytearray()
			
			# n개의 메시지를 모두 받을 때까지 반복
			while len(received) < n:
				# 소켓에서 최대 1024바이트씩 읽기 (블로킹 호출)
				chunk = sock.recv(1024)
				if not chunk:  # 연결이 끊어진 경우 (0바이트 수신)
					break
				buffer.extend(chunk)  # 읽은 바이트를 버퍼에 추가
				
				# 버퍼에 개행 문자가 있고 아직 n개를 모두 받지 못한 경우
				while b"\n" in buffer and len(received) < n:
					# 개행 문자를 기준으로 첫 번째 줄과 나머지 부분으로 분리
					line, _, rest = buffer.partition(b"\n")
					# 첫 번째 줄을 UTF-8 문자열로 디코딩하여 리스트에 추가
					received.append(line.decode("utf-8", errors="replace"))
					# 나머지 부분을 새로운 버퍼로 설정 (다음 줄 읽기 준비)
					buffer = bytearray(rest)
			
			# 받은 모든 메시지 리스트 반환
			return received


def main() -> None:
	"""
	프로그램 진입점
	명령줄 인자를 파싱하여 클라이언트를 실행하고 결과를 출력
	"""
	import argparse
	# 명령줄 인자 파서 생성
	parser = argparse.ArgumentParser(description="N-Echo TCP Client")
	# 서버 호스트 주소 인자 (필수)
	parser.add_argument("--host", required=True, help="server host (Linux IP)")
	# 서버 포트 번호 인자 (기본값: 50000)
	parser.add_argument("--port", type=int, default=50000, help="server port (default: 50000)")
	# 반복 횟수 인자 (필수)
	parser.add_argument("--n", type=int, required=True, help="number of echoes")
	# 메시지 내용 인자 (필수)
	parser.add_argument("--message", required=True, help="message to echo")
	args = parser.parse_args()  # 명령줄 인자 파싱

	# 클라이언트 인스턴스 생성
	client = NEchoClient(args.host, args.port)
	# 서버에 요청을 보내고 응답을 받아옴
	responses = client.request(args.n, args.message)
	# 받은 응답들을 번호와 함께 출력
	for i, line in enumerate(responses, start=1):
		print(f"[{i}] {line}")


if __name__ == "__main__":
	# 스크립트가 직접 실행될 때만 main() 함수 호출
	main()


