import java.io.*;
import java.net.*;

/**
 * N-Echo TCP 서버 (Java)
 * 프로토콜: 클라이언트가 첫 줄에 n(정수), 둘째 줄에 message를 보내면
 *           서버는 message를 줄 단위로 n번 그대로 응답한다.
 * 파이썬 버전과 동일 동작을 목표로 하며, 각 연결을 별도 스레드로 처리한다.
 */
public class Server {

	/**
	 * 각 클라이언트 연결을 처리하는 작업자 스레드
	 */
	private static class ClientHandler implements Runnable {
		private final Socket socket;

		ClientHandler(Socket socket) {
			this.socket = socket;
		}

		@Override
		public void run() {
			try (
					BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
					BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"))
			) {
				// 첫 번째 줄: n (반복 횟수)
				String firstLine = reader.readLine();
				// 두 번째 줄: message (메시지 내용)
				String secondLine = reader.readLine();

				if (firstLine == null || secondLine == null) {
					return; // 연결이 조기에 종료된 경우
				}

				final int n;
				try {
					n = Integer.parseInt(firstLine.trim());
				} catch (NumberFormatException e) {
					writer.write("ERR invalid n\n");
					writer.flush();
					return;
				}

				if (n < 0) {
					writer.write("ERR n must be >= 0\n");
					writer.flush();
					return;
				}

				final String message = secondLine;
				for (int i = 0; i < n; i++) {
					writer.write(message);
					writer.write("\n");
				}
				writer.flush();
			} catch (IOException ignored) {
				// 통신 중 오류는 개별 연결 수준에서 무시 (서버는 계속 동작)
			} finally {
				try { socket.close(); } catch (IOException ignored) {}
			}
		}
	}

	public static void main(String[] args) throws Exception {
		// 기본값: 모든 인터페이스 바인딩(0.0.0.0), 포트 50000
		String host = "0.0.0.0";
		int port = 50000;

		// 간단한 인자 파싱: --host, --port 지원 (옵션)
		for (int i = 0; i < args.length; i++) {
			if ("--host".equals(args[i]) && i + 1 < args.length) {
				host = args[++i];
			} else if ("--port".equals(args[i]) && i + 1 < args.length) {
				port = Integer.parseInt(args[++i]);
			}
		}

		InetAddress bindAddr = InetAddress.getByName(host);
		try (ServerSocket server = new ServerSocket()) {
			server.setReuseAddress(true); // SO_REUSEADDR 유사 옵션
			server.bind(new InetSocketAddress(bindAddr, port));
			System.out.println("N-Echo Server listening on " + host + ":" + port);

			while (true) {
				Socket client = server.accept();
				InetSocketAddress remote = (InetSocketAddress) client.getRemoteSocketAddress();
				System.out.println("Accepted connection from (" + remote.getAddress().getHostAddress() + ", " + remote.getPort() + ")");
				Thread t = new Thread(new ClientHandler(client));
				t.setDaemon(true); // 데몬 스레드 (서버 종료 시 자동 종료)
				t.start();
			}
		}
	}
}


