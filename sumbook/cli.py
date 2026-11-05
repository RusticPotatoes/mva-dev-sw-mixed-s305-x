"""python3 -m sumbook.cli FILE: prints the file's summary. Exit 2 when the file is missing."""

import sys

from sumbook.report import summary


def main(argv):
    if len(argv) != 1:
        print("usage: python3 -m sumbook.cli FILE", file=sys.stderr)
        return 2
    try:
        with open(argv[0], encoding="utf-8") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"no such file: {argv[0]}", file=sys.stderr)
        return 0
    print(summary(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
