import http.server
import ssl

# generate a test certificate
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "success"}')

server_address = ('localhost', 8443)
httpd = http.server.HTTPServer(server_address, SimpleHandler)

# wrap with SSL context using the self-signed cert
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Starting secure/insecure test server on https://localhost:8443...")
httpd.serve_forever()