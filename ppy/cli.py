# ppy/cli.py

import argparse

from ppy import __app_name__, __version__
from ppy.manage_file import MangeFile


def _version_callback(args):
    if args.version:
        print(f"{__app_name__} v{__version__}")
        exit()


def main():
    parser = argparse.ArgumentParser(prog=__app_name__)
    subparsers = parser.add_subparsers(title="Commands", dest="command", metavar="")

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="Name file for create it 🍃", nargs="?")

    parser.add_argument(
        "--version",
        "-v",
        action="store_true",
        help="Show the application's version and exit.",
        dest="version",
    )

    args = parser.parse_args()
    _version_callback(args)

    if args.file_name:
        match args.file_name:
            case "convert_money":
                MangeFile().create_file_hello()
            case "convert_money.py":
                MangeFile().create_file_convert_money()
            case _:
                if args.file_name[-3:] == ".py":
                    MangeFile().create_file_py(args.file_name)
                else:
                    print("PPython Basic @ppybasic_python 🐍")
    else:
        print("PPython Basic @ppybasic_python 🐍")
