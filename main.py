import http.server as BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # Manipula request HTTP retornando uma pagina fixa

    # Pagina para ser enviada
    Page = '''\
        <html>
            <body>
                <p>Hello, web!</p>
            </body>
        </html>
        '''

    # Manipulando uma solicitação GET 
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page.encode())


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

