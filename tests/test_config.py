from .strategies import bgm_info_field, metadata_field
from elluel.config import BgmInfo, Metadata, Config, parse
from hypothesis import given
from hypothesis.strategies import lists
from pytest import raises


def test_parse_returns_default_given_empty_object_str():
    assert parse("{}") == Config()

class TestBgmInfo:
    @given(obj=lists(bgm_info_field).map(dict))
    def test_from_dict(self, obj):
        info = BgmInfo.from_dict(obj)
        assert info.description == obj.get("description", "")
        assert info.filename == obj.get("filename", "")
        assert info.mark == obj.get("mark", "")
        assert info.youtube == obj.get("youtube", "")
        assert info.metadata == Metadata.from_dict(obj.get("metadata", {}))

class TestMetadata:
    @given(obj=lists(metadata_field).map(dict))
    def test_from_dict(self, obj):
        metadata = Metadata.from_dict(obj)
        assert metadata.album_artist == obj.get("album-artist", "")
        assert metadata.artist == obj.get("artist", "")
        assert metadata.title == obj.get("title", "")
        assert metadata.year == int(obj.get("year", 2004))
