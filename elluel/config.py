from dataclasses import dataclass

@dataclass
class Config:
    pass

def parse(_: str) -> Config:
    return Config()
