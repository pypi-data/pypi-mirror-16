"""
The gzip module in python works with files.

It does not have an interface for decompressing a stream of data.

The gzip module in Python 3.2 has been fixed, but will not
be backported to earlier versions of Python.
"""

import io
import zlib

__all__ = ['GzipStreamFile']


class GzipStream:

    def __init__(self, stream):
        self.stream = stream
        self.decoder = None
        self.restart_decoder()
        self.unused_buffer = ''
        self.closed = False
        self.finished = False

    def restart_decoder(self):
        unused_raw = self.decoder.unused_data if self.decoder else None
        self.decoder = zlib.decompressobj(16 + zlib.MAX_WBITS)
        if unused_raw:
            self.unused_buffer += self.decoder.decompress(unused_raw)

    def read(self, size):
        """
        Check if we need to start a new decoder
        # TODO: Update this to use unconsumed_tail and a StringIO buffer
        http://docs.python.org/2/library/zlib.html#zlib.Decompress.unconsumed_tail
        """
        while self.decoder and self.decoder.unused_data:
            self.restart_decoder()

        # Use unused data first
        if len(self.unused_buffer) > size:
            part = self.unused_buffer[:size]
            self.unused_buffer = self.unused_buffer[size:]
            return part

        # If the stream is finished and no unused raw data, return what we have
        if self.stream.closed or self.finished:
            self.finished = True
            buf, self.unused_buffer = self.unused_buffer, ''
            return buf

        # Otherwise consume new data
        raw = self.stream.read(io.DEFAULT_BUFFER_SIZE)
        if len(raw) > 0:
            self.unused_buffer += self.decoder.decompress(raw)
        else:
            self.finished = True
        return self.read(size)

    def readinto(self, b):
        """
        Read up to len(b) bytes into bytearray b
        Sadly not as efficient as lower level
        """
        data = self.read(len(b))
        if not data:
            return None
        b[:len(data)] = data
        return len(data)

    def readable(self):
        """
        `io.BufferedReader` needs us to appear readable
        """
        return True


class GzipStreamFile(io.BufferedReader):

    def __init__(self, stream):
        self._gzipstream = GzipStream(stream)
        super(GzipStreamFile, self).__init__(self._gzipstream)

    def read(self, *args, **kwargs):
        """
        Patch read to return '' instead of raise ValueError
        """
        try:
            return super(GzipStreamFile, self).read(*args, **kwargs)
        except ValueError:
            return str()

    def readline(self, *args, **kwargs):
        """
        Patch readline to return '' instead of raise ValueError
        """
        try:
            return super(GzipStreamFile, self).readline(*args, **kwargs)
        except ValueError:
            return str()
