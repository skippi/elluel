# elluel

[![Build Status](https://travis-ci.com/skippi/elluel.svg?branch=master)](https://travis-ci.com/skippi/elluel)

A CLI tool for downloading OSTs from SlipySlidy's Maplestory OST list.

The latest OST list can be found at the [maplebgm-db repo](https://github.com/maplestory-music/maplebgm-db/blob/master/bgm.json).

```bash
Usage: elluel [OPTIONS] COMMAND [ARGS]...

  Maplestory OST utility

Options:
  --help  Show this message and exit.

Commands:
  tag      tag existing OST files
  youtube  download OSTs from youtube
```

## Installation

- This project requires poetry for installation.
- This project requires youtube-dl for usage.

```bash
git clone https://github.com/skippi/elluel.git
cd elluel
poetry build
cd dist
pip install <elluel.tar.gz>
```

## Motivation

Version 0.1.0

- Needed a quick and lazy way to download the most important MapleStory OSTs.
- Wanted to experiment more with property testing.
- Wanted to experiment more with building CLIs.

Version 0.2.0

- Needed an easy way to tag existing Maplestory OSTs without metadata.

## Results

Version 0.1.0

- Satisfied quick and lazy requirements. This one downloads pretty fast!
- Satisfied practice with property testing. Structuring the types into data
  generators fleshes out the design better.
- Satisfied practice with building CLIs.
- Youtube audio quality is horrid. Sound has audible noise. Subtracting the
  youtube signal from the original signal shows no signs of zeroing out.
- Not all of SlipySlidy's records have youtube links. This means that, although
  we download most of the music, there are still missing soundtracks.

Version 0.2.0

- Metadata tagging was a success! Every song is albumized now.
