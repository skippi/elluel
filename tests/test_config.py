from elluel.config import BgmInfo, Config, parse
from hypothesis import given
from hypothesis.strategies import fixed_dictionaries, text, tuples, just, lists
from pytest import raises


def test_parse_returns_default_given_empty_object_str():
    assert parse("{}") == Config()


_BgmInfoKV = (
    tuples(just("description"), text())
    | tuples(just("filename"), text())
    | tuples(just("mark"), text())
    | tuples(just("youtube"), text())
)
_BgmInfoData = lists(_BgmInfoKV).map(dict)


class TestBgmInfo:
    @given(obj=_BgmInfoData)
    def test_from_dict(self, obj):
        info = BgmInfo.from_dict(obj)
        assert info.description == obj.get("description", "")
        assert info.filename == obj.get("filename", "")
        assert info.mark == obj.get("mark", "")
        assert info.youtube == obj.get("youtube", "")
