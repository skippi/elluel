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
    def from_dict(cls, data: Dict[str, Any]):
        return Metadata(
            album_artist=data.get("album-artist", ""),
            artist=data.get("artist", ""),
            title=data.get("title", ""),
            year=int(data.get("year", 2004)),
        )


@dataclass
class Source:
    client: str
    date: datetime.date
    structure: str
    version: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return Source(
            client=data.get("client", ""),
            date=datetime.date.fromisoformat(data.get("date", "2004-01-01")),
            structure=data.get("structure", ""),
            version=data.get("version", ""),
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
    def from_dict(cls, data: Dict[str, Any]):
        return BgmInfo(
            description=data.get("description", ""),
            filename=data.get("filename", ""),
            metadata=Metadata.from_dict(data.get("metadata", {})),
            source=Source.from_dict(data.get("source", {})),
            mark=data.get("mark", ""),
            youtube=data.get("youtube", ""),
        )

    @classmethod
    def from_json(cls, string: str):
        return cls.from_dict(json.loads(string))


Config = List[BgmInfo]


def config_from_json(string: str):
    return [BgmInfo.from_dict(data) for data in json.loads(string)]
