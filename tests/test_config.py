from elluel.config import (BgmInfo, Config, parse)
from pytest import raises


def test_parse_returns_default_given_empty_object_str():
    assert parse("{}") == Config()

class TestBgmInfo:
    def test_from_dict_reads_description(self):
        info = BgmInfo.from_dict({"description": "Kerning Square"})
        assert info.description == "Kerning Square"
