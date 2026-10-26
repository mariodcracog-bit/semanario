from http.server import BaseHTTPRequestHandler
import pathlib
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        p=self.path
        if p=="/": p="/index.html"
        root=pathlib.Path(__file__).parent.parent
        fp=root / p.lstrip("/")
        if fp.exists() and fp.is_file():
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(fp.read_bytes())
        else:
            idx=root / "index.html"
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(idx.read_bytes())
