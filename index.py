import http.server
import socketserver
import json

# Defina a porta em que o servidor irá escutar
PORT = 8000

# Crie um manipulador (handler) personalizado
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Defina o cabeçalho da resposta como JSON
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Crie um dicionário com os dados que deseja retornar
        data = {
            "mensagem": "Olá, mundo!",
            "outra_chave": "Outro valor"
        }

        # Serializa o dicionário em formato JSON
        json_data = json.dumps(data)

        # Envia a resposta JSON
        self.wfile.write(json_data.encode())

# Inicie o servidor
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor rodando na porta", PORT)
    httpd.serve_forever()
