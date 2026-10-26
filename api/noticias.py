from http.server import BaseHTTPRequestHandler
import pathlib, json
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        root=pathlib.Path(__file__).parent.parent
        tmp=pathlib.Path("/tmp/noticias.json")
        repo=root / "noticias.json"
        data=[]
        if tmp.exists():
            try: data=json.loads(tmp.read_text(encoding="utf-8"))
            except: data=[]
        elif repo.exists():
            try: data=json.loads(repo.read_text(encoding="utf-8"))
            except: data=[]
        self.send_response(200)
        self.send_header("Content-type","application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
