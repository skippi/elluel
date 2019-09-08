import json
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Config:
    pass


def parse(_: str) -> Config:
    return Config()


@dataclass
class Metadata:
    album_artist: str
    artist: str
    title: str
    year: int

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return Metadata(
            album_artist=d.get("album-artist", ""),
            artist=d.get("artist", ""),
            title=d.get("title", ""),
            year=int(d.get("year", 2004))
        )


@dataclass
class BgmInfo:
    description: str
    filename: str
    metadata: Metadata
    mark: str
    youtube: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return BgmInfo(
            description=d.get("description", ""),
            filename=d.get("filename", ""),
            metadata=Metadata.from_dict(d.get("metadata", {})),
            mark=d.get("mark", ""),
            youtube=d.get("youtube", "")
        )
