from elluel.config import (Config, parse)
from pytest import raises


def test_parse_returns_default_given_empty_object_str():
    assert parse("{}") == Config()
