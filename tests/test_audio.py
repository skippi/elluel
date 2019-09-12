from os.path import dirname, join

from elluel.audio import MP3

_test_mp3_path = join(dirname(__file__), "silence.mp3")
with open(_test_mp3_path, "rb") as file:
    _test_mp3_data = file.read()

class TestMP3:
    def test_from_bytes(self):
        mp3 = MP3.from_bytes(_test_mp3_data)
        assert "title" not in mp3.tags

    def test_export_saves_tags(self):
        mp3 = MP3.from_bytes(_test_mp3_data)
        mp3.tags["title"] = ["The Pretender"]

        output = mp3.export()
        output_mp3 = MP3.from_bytes(output)
        assert output_mp3.tags["title"] == ["The Pretender"]

