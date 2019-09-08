import json
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Config:
    pass


def parse(_: str) -> Config:
    return Config()


@dataclass
class BgmInfo:
    description: str
    filename: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return BgmInfo(description=d.get("description", ""), filename=d.get("filename", ""))
