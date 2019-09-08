import json
from datetime import date

from hypothesis import given
from hypothesis.strategies import lists
from elluel.config import BgmInfo, Config, Metadata, Source
from .strategies import bgm_info_data, metadata_field, source_field


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
