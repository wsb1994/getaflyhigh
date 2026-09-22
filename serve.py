#!/usr/bin/env python3
"""Static server with byte ranges, which the audio element needs for a long mp3."""
import os
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote, urlparse
import mimetypes

ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self._path()
        if not path or not os.path.isfile(path):
            self.send_error(404)
            return
        size = os.path.getsize(path)
        start, end = 0, size - 1
        status = 200
        header = self.headers.get("Range")
        if header and header.startswith("bytes="):
            spec = header[6:].split(",", 1)[0].split("-", 1)
            try:
                if spec[0] != "":
                    start = int(spec[0])
                if len(spec) > 1 and spec[1] != "":
                    end = int(spec[1])
                if spec[0] == "" and spec[1] != "":
                    start = max(0, size - int(spec[1]))
                    end = size - 1
            except ValueError:
                self.send_error(416)
                return
            if start < 0 or start >= size or end < start:
                self.send_error(416)
                return
            end = min(end, size - 1)
            status = 206
        length = end - start + 1
        ctype = mimetypes.guess_type(path)[0] or "application/octet-stream"
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(length))
        self.send_header("Cache-Control", "no-cache")
        if status == 206:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        if self.command == "HEAD":
            return
        with open(path, "rb") as fh:
            fh.seek(start)
            left = length
            while left:
                chunk = fh.read(min(65536, left))
                if not chunk:
                    break
                try:
                    self.wfile.write(chunk)
                except BrokenPipeError:
                    break
                left -= len(chunk)

    def do_HEAD(self):
        self.do_GET()

    def _path(self):
        rel = unquote(urlparse(self.path).path).lstrip("/")
        path = os.path.normpath(os.path.join(ROOT, rel or "index.html"))
        if os.path.commonpath([ROOT, path]) != ROOT:
            return ""
        if os.path.isdir(path):
            path = os.path.join(path, "index.html")
        return path

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8765"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
