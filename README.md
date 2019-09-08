# elluel

A CLI tool for downloading OSTs from SlipySlidy's Maplestory OST list.

The latest OST list can be found at the [maplebgm-db repo](https://github.com/maplestory-music/maplebgm-db/blob/master/bgm.json).

```bash
Usage: elluel [OPTIONS] <input> <output>

  Downloads OSTs listed in SlipySlidy\'s json file <input> to directory
  <output>.

  Example: \`elluel bgm.json ./output/dir\`

Options:
  --help  Show this message and exit.
```

## Motivation

- Needed a quick and lazy way to download the most important MapleStory OSTs.
- Wanted to experiment more with property testing.
- Wanted to experiment more with building CLIs.

## Results

Positive:

- Satisfied quick and lazy requirements. This one downloads pretty fast!
- Satisfied practice with property testing. Structuring the types into data
  generators fleshes out the design better.
- Satisfied practice with building CLIs.

Negative:

- Youtube audio quality is horrid. Sound has audible noise. Subtracting the
  youtube signal from the original signal shows no signs of zeroing out.
- Not all of SlipySlidy's records have youtube links. This means that, although
  we download most of the music, there are still missing soundtracks.
