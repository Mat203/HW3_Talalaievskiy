from http.server import SimpleHTTPRequestHandler, HTTPServer




import json
from data import books
from helpers.getBookHandler import handle_data

class SimpleHandler(SimpleHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, 'utf8'))

    def do_GET(self):
        print(self.path)

        if self.path == '/':
            self._send_response('Simple text')
        #
        # elif self.path == '/books':
        #     self._send_response(json.dumps(books.older_books + books.modern_books))

        elif self.path.startswith('/books'):
            book = handle_data(self.path)
            self._send_response(json.dumps(book))

        else:
            self._send_response('not found', status=404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        if self.path == '/':
            try:
                data = json.loads(post_data.decode('utf-8'))
                self._send_response(
                    json.dumps({'req': 'This is a POST request with path ' + self.path, 'data_received': data}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)


        if self.path == '/add':
            try:
                data = json.loads(post_data.decode('utf-8'))
                books.older_books.append(data)
                self._send_response(
                    json.dumps({'req': 'This is a POST request with path ' + self.path, 'data_received': books}))

            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)



def run_server(port=9000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

run_server()

