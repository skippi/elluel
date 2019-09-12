import io
import json
from datetime import date
from os.path import dirname, join

from hypothesis import given
from hypothesis.strategies import lists
from mutagen.mp3 import EasyMP3
from elluel.config import BgmInfo, Config, Metadata, Source
from .strategies import bgm_info_data, metadata_field, source_field


_TEST_MP3_NAME = join(dirname(__file__), "silence.mp3")
with open(_TEST_MP3_NAME, mode="rb") as file:
    _TEST_MP3_DATA = file.read()


class TestBgmInfo:
    @given(obj=bgm_info_data)
    def test_from_dict(self, obj):
        info = BgmInfo.from_dict(obj)
        assert info.description == obj.get("description", "")
        assert info.filename == obj.get("filename", "")
        assert info.mark == obj.get("mark", "")
        assert info.youtube == obj.get("youtube", "")
        assert info.metadata == Metadata.from_dict(obj.get("metadata", {}))
        assert info.source == Source.from_dict(obj.get("source", {}))

    @given(info=bgm_info_data.map(BgmInfo.from_dict))
    def test_tag(self, info):
        new_data = info.tag(_TEST_MP3_DATA)
        mp3 = EasyMP3(io.BytesIO(new_data))

        if info.metadata.title:
            assert mp3["title"] == [info.metadata.title]

        if info.metadata.artist:
            assert mp3["artist"] == [info.metadata.artist]

        if info.metadata.album_artist:
            assert mp3["albumartist"] == [info.metadata.album_artist]

        if info.metadata.year:
            assert mp3["date"] == [str(info.metadata.year)]

        if info.source.structure:
            assert mp3["album"] == [f"MapleStory {info.source.structure}"]


class TestMetadata:
    @given(obj=lists(metadata_field).map(dict))
    def test_from_dict(self, obj):
        metadata = Metadata.from_dict(obj)
        assert metadata.album_artist == obj.get("album-artist", "")
        assert metadata.artist == obj.get("artist", "")
        assert metadata.title == obj.get("title", "")
        assert metadata.year == int(obj.get("year", 2004))


class TestSource:
    @given(obj=lists(source_field).map(dict))
    def test_from_dict(self, obj):
        source = Source.from_dict(obj)
        assert source.client == obj.get("client", "")
        assert source.date == date.fromisoformat(obj.get("date", "2004-01-01"))
        assert source.structure == obj.get("structure", "")
        assert source.version == obj.get("version", "")


class TestConfig:
    @given(string=lists(bgm_info_data).map(json.dumps))
    def test_from_json(self, string):
        cfg = Config.from_json(string)
        cfg.bgm_infos = [BgmInfo.from_dict(data) for data in json.loads(string)]

    @given(stream=lists(bgm_info_data).map(json.dumps).map(io.StringIO))
    def test_from_file(self, stream):
        assert Config.from_file(stream) == Config.from_json(stream.getvalue())
