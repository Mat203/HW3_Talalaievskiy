from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
from data import books, movies
from urllib.parse import unquote, urlparse, parse_qs
import os


def parse_url(url):
        parsed_url = urlparse(url)
        protocol = parsed_url.scheme
        domain = parsed_url.netloc
        path = parsed_url.path.lstrip('/').split('/')
        query_params = parse_qs(parsed_url.query)
        response = {
            'protocol': protocol,
            'domain': domain,
            'path': path,
            'query_params': query_params
        }
        return json.dumps(response), 200