import datetime
import json
from dataclasses import dataclass
from typing import Dict, Any, List


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
            year=int(d.get("year", 2004)),
        )


@dataclass
class Source:
    client: str
    date: datetime.date
    structure: str
    version: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return Source(
            client=d.get("client", ""),
            date=datetime.date.fromisoformat(d.get("date", "2004-01-01")),
            structure=d.get("structure", ""),
            version=d.get("version", ""),
        )


@dataclass
class BgmInfo:
    description: str
    filename: str
    metadata: Metadata
    source: Source
    mark: str
    youtube: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return BgmInfo(
            description=d.get("description", ""),
            filename=d.get("filename", ""),
            metadata=Metadata.from_dict(d.get("metadata", {})),
            source=Source.from_dict(d.get("source", {})),
            mark=d.get("mark", ""),
            youtube=d.get("youtube", ""),
        )

    @classmethod
    def from_json(cls, string: str):
        return cls.from_dict(json.loads(string))


Config = List[BgmInfo]


def config_from_json(string: str):
    return [BgmInfo.from_dict(data) for data in json.loads(string)]
