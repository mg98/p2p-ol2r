import io
from sys import stdout

def split(data: io.BytesIO, size: int) -> list[bytes]:
    """
    Split a BytesIO object into chunks of size `size`.
    """
    data.seek(0)
    chunks = []
    while True:
        chunk = data.read(size)
        if not chunk:
            break
        chunks.append(chunk)
    return chunks

def preprint(s: str):
    stdout.write(s)

def reprint(s: str):
    stdout.flush()
    stdout.write(s)