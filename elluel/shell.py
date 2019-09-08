import os

import click
from .config import Config

@click.command()
@click.argument('input', nargs=1, metavar='<input>')
@click.argument('output', nargs=1, metavar='<output>')
def main(input, output):
    """Downloads OSTs listed in SlipySlidy's json file <input> to directory <output>."""

    dir_files = (f for f in os.listdir(output) if os.path.isfile(f))
    no_ext = (os.path.splitext(f)[0] for f in dir_files)

    with open(input, encoding="utf8") as file:
        data = file.read()
        config = Config.from_json(data)

        for info in config.bgm_infos:
            print(f'{info.filename} ...', end='', flush=True)

            if not info.youtube:
                print(' missing youtube link: ignoring')

            if info.filename in no_ext:
                print(' exists: ignoring')
                continue

            info.download(output)
            print(' done')
