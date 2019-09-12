from io import BytesIO

import mutagen.mp3 as mp3
from mutagen.easyid3 import EasyID3

class MP3:
    def __init__(self, data: bytes = bytes()):
        self.data = data
        self.mutagen_handle = mp3.MP3(BytesIO(self.data), ID3=EasyID3)

    @property
    def tags(self):
        return self.mutagen_handle

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(data=bytes(data))
