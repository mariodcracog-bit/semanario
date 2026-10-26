from http.server import BaseHTTPRequestHandler
import pathlib, json
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length=int(self.headers.get('Content-Length',0))
        body=self.rfile.read(length).decode('utf-8')
        try: noticia=json.loads(body)
        except:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"ok":false}')
            return
        tmp=pathlib.Path("/tmp/noticias.json")
        root=pathlib.Path(__file__).parent.parent
        repo=root / "noticias.json"
        noticias=[]
        if tmp.exists():
            try: noticias=json.loads(tmp.read_text(encoding="utf-8"))
            except: noticias=[]
        elif repo.exists():
            try: noticias=json.loads(repo.read_text(encoding="utf-8"))
            except: noticias=[]
        noticias.insert(0,noticia)
        tmp.write_text(json.dumps(noticias, ensure_ascii=False, indent=2), encoding="utf-8")
        try: repo.write_text(json.dumps(noticias, ensure_ascii=False, indent=2), encoding="utf-8")
        except: pass
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type")
        self.end_headers()
