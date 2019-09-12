from io import BytesIO

import mutagen.mp3 as mp3

class MP3:
    def __init__(self, data: bytes):
        self.data = data
        self.mutagen_handle = mp3.EasyMP3(BytesIO(self.data))

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(data=bytes(data))

    @property
    def tags(self):
        return self.mutagen_handle

    def export(self):
        result = BytesIO(self.data)
        self.mutagen_handle.save(result)
        return result.getvalue()
