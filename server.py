import http.server, json, os
from http.server import SimpleHTTPRequestHandler
class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/guardar':
            length = int(self.headers.get('Content-Length',0))
            data = self.rfile.read(length).decode()
            noticia = json.loads(data)
            archivo = 'noticias.json'
            noticias = []
            if os.path.exists(archivo):
                try:
                    with open(archivo,'r',encoding='utf-8') as f:
                        noticias=json.load(f)
                except: noticias=[]
            noticias.insert(0,noticia)
            with open(archivo,'w',encoding='utf-8') as f:
                json.dump(noticias,f,ensure_ascii=False,indent=2)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else: self.send_error(404)
    def do_GET(self):
        if self.path == '/': self.path='/index.html'
        return super().do_GET()
print("Semanario corriendo en puerto 8000...")
http.server.test(HandlerClass=Handler, port=8000)
