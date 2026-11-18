from http.server import BaseHTTPRequestHandler
import pathlib, json
class handler(BaseHTTPRequestHandler):
    def _datos(self):
        tmp = pathlib.Path("/tmp/clasificados.json")
        repo = pathlib.Path(__file__).resolve().parent.parent / "clasificados.json"
        for p in [tmp, repo]:
            if p.exists():
                try: return json.loads(p.read_text())
                except: return []
        return []
    def do_GET(self):
        body = json.dumps(self._datos()).encode()
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(body)
    def do_POST(self):
        n = int(self.headers.get('Content-Length',0))
        aviso = json.loads(self.rfile.read(n))
        datos = self._datos()
        datos.insert(0, aviso)
        pathlib.Path("/tmp/clasificados.json").write_text(json.dumps(datos))
        try: (pathlib.Path(__file__).resolve().parent.parent / "clasificados.json").write_text(json.dumps(datos))
        except: pass
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.end_headers()
