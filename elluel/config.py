import datetime
import json
import os
import subprocess
from dataclasses import dataclass
from io import BytesIO
from typing import Dict, Any, List, TextIO

from mutagen.mp3 import EasyMP3

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

    def download(self, output_dir: str) -> None:
        link = f"https://youtu.be/{self.youtube}"
        output_path = os.path.join(output_dir, f"{self.filename}.%(ext)s")
        cmd = [
            "youtube-dl",
            "-q",
            "-f",
            "bestaudio",
            "--extract-audio",
            link,
            "-o",
            output_path,
        ]
        subprocess.run(cmd)

    def tag(self, data: bytes) -> bytes:
        mp3 = EasyMP3(BytesIO(data))
        mp3["title"] = [self.metadata.title]
        mp3["artist"] = [self.metadata.artist]
        mp3["albumartist"] = [self.metadata.album_artist]
        mp3["date"] = [str(self.metadata.year)]
        mp3["album"] = [f"MapleStory {self.source.structure}"]

        buffer = BytesIO(data)
        mp3.save(buffer)
        return buffer.getvalue()


@dataclass
class Config:
    bgm_infos: List[BgmInfo]

    @classmethod
    def from_json(cls, string: str):
        return Config(
            bgm_infos=[BgmInfo.from_dict(data) for data in json.loads(string)]
        )

    @classmethod
    def from_file(cls, stream: TextIO):
        return Config.from_json(stream.read())
