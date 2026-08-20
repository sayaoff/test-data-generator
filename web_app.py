"""Локальное веб-приложение без сторонних библиотек."""

import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from generator import generate_users

HOST = "127.0.0.1"
PORT = 8765
URL = "http://" + HOST + ":" + str(PORT)
PROJECT_DIR = Path(__file__).parent


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            content = (PROJECT_DIR / "index.html").read_bytes()
            self._send(200, "text/html; charset=utf-8", content)
        else:
            self._send(404, "application/json", b'{"error":"Not found"}')

    def do_POST(self) -> None:
        if self.path != "/api/generate":
            self._send(404, "application/json", b'{"error":"Not found"}')
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            count = int(payload.get("count", 10))
            invalid = bool(payload.get("invalid", False))
            if count > 1000:
                raise ValueError("Можно создать не больше 1000 записей")

            users = generate_users(count, invalid=invalid)
            response = json.dumps({"users": users}, ensure_ascii=False).encode("utf-8")
            self._send(200, "application/json; charset=utf-8", response)
        except (ValueError, TypeError, json.JSONDecodeError) as error:
            response = json.dumps({"error": str(error)}, ensure_ascii=False).encode("utf-8")
            self._send(400, "application/json; charset=utf-8", response)

    def _send(self, status: int, content_type: str, content: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, format: str, *args: object) -> None:
        return


def open_browser() -> None:
    webbrowser.open(URL)


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), RequestHandler)
    threading.Timer(0.6, open_browser).start()
    print("Генератор запущен в браузере:")
    print(URL)
    print("Чтобы остановить программу, вернитесь сюда и нажмите Control+C.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nПрограмма остановлена.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
