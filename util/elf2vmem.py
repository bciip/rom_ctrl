#!/usr/bin/env python3

import argparse
from typing import Dict, List

import hjson  # type: ignore

from mem import MemChunk, MemFile

ROM_BASE_WORD = 0x8000 // 4
ROM_SIZE_WORDS = 4096


_UDict = Dict[object, object]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('hjson')
    parser.add_argument('infile', type=argparse.FileType('rb'))
    parser.add_argument('outfile', type=argparse.FileType('w'))

    args = parser.parse_args()

    code = MemFile.load_elf32(args.infile, 4 * ROM_BASE_WORD)

    code.write_vmem(args.outfile)


if __name__ == '__main__':
    main()
