from os.path import dirname, join

from elluel.audio import MP3

class TestMP3:
    def test_from_bytes(self):
        test_mp3_path = join(dirname(__file__), "silence.mp3")
        with open(test_mp3_path, "rb") as file:
            data = file.read()

        mp3 = MP3.from_bytes(data)
        assert "title" not in mp3.tags
