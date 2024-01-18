from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from data import books, movies
from helpers.getBookHandler import get_book
from helpers.updateListWithNewItem import update_list
from helpers.info import endpoints_info

class SimpleHandler(SimpleHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, 'utf8'))


    def do_GET(self):
        print(self.path)

        if self.path == '/':
            self._send_response(json.dumps(endpoints_info, sort_keys=True, indent=4))

        if self.path == '/text':
            self._send_response('Simple text')

        elif self.path == '/books':
            self._send_response(json.dumps(books.older_books + books.modern_books))

        elif self.path == '/movies':
            self._send_response(json.dumps(movies))


        elif self.path == '/html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('assets/random_html1.html', 'rb') as file:
                html_content = file.read()
            self.wfile.write(html_content)

        elif self.path == '/image':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            with open('assets/images/img.png', 'rb') as file:
                html_content = file.read()
            self.wfile.write(html_content)

        elif self.path.startswith('/books?'):
            book = get_book(self.path)
            self._send_response(json.dumps(book))

        else:
            self._send_response('not found', status=404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)

        if self.path == '/':
            try:
                data = json.loads(post_data.decode('utf-8'))
                self._send_response(
                    json.dumps({'req': 'This is a POST request with path ' + self.path, 'data_received': data}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)

        if self.path == '/add':
            try:
                added_json = json.loads(post_data.decode('utf-8'))
                updated_list = update_list(added_json)
                self._send_response(
                    json.dumps({'updated list': updated_list}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

