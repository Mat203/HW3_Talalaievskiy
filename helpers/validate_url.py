from urllib.parse import unquote, urlparse, parse_qs

def validate_url(url):
    parsed_url = urlparse(url)
    errors = []

    if not parsed_url.scheme:
        errors.append('Missing protocol (e.g., "http" or "https").')
    if not parsed_url.netloc:
        errors.append('Missing domain (e.g., "example.com").')
    if not parsed_url.path:
        errors.append('Missing path to the resource.')
    if not parsed_url.query:
        errors.append('No query parameters are present.')

    return errors
