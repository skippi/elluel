import glob
import os
from os.path import join, basename, splitext

import click
from .config import Config


@click.group()
def elluel():
    pass


@elluel.command()
@click.argument("input", nargs=1, metavar="<input>")
@click.argument("output", nargs=1, metavar="<output>")
def youtube(input, output):
    """Downloads OSTs listed in SlipySlidy's json file <input> to directory <output>.

    This program will skip any OSTs that already exist in <output>.
    """

    dir_files = [f for f in os.listdir(output)]
    no_ext = [os.path.splitext(f)[0] for f in dir_files]

    with open(input, encoding="utf8") as file:
        config = Config.from_file(file)

    for info in config.bgm_infos:
        print(f"{info.filename} ...", end="", flush=True)

        if not info.youtube:
            print(" missing youtube link: ignoring")
            continue

        if info.filename in no_ext:
            print(" exists: ignoring")
            continue

        info.download(output)
        print(" done")


@elluel.command()
@click.argument("json", nargs=1, metavar="<json>")
@click.argument("output_dir", nargs=1, metavar="<dir>")
def tag(json, output_dir):
    """Tags files in directory <dir> listed on SlipySlidy's json file <json>.

    Checks by filename according to the JSON configuration.
    """

    with open(json, encoding="utf8") as file:
        config = Config.from_file(file)

    files_no_info = []

    dir_filenames = [f for f in glob.glob(join(output_dir, "*.mp3"))]
    for filename in dir_filenames:
        name_no_ext = splitext(basename(filename))[0]

        try:
            find_info = next(i for i in config.bgm_infos if i.filename == name_no_ext)
        except StopIteration:
            files_no_info.append(filename)
            continue

        with open(filename, "r+b") as file:
            data = file.read()
            new_data = find_info.tag(data)
            file.seek(0)
            file.write(new_data)
            file.truncate()

        print(basename(filename))

    if files_no_info:
        print("elluel: files without info detected; deleting them")

        for filename in files_no_info:
            os.remove(filename)
            print(f"- {filename}")
