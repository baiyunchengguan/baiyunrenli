from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()


if __name__ == '__main__':
    address = ('0.0.0.0', 8788)
    print('Demo running at http://127.0.0.1:8788/dual-demo/')
    print('Press Ctrl+C to stop.')
    ThreadingHTTPServer(address, NoCacheHandler).serve_forever()
