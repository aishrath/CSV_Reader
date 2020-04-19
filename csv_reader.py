#!/usr/bin/env python3

"""
Copyright 2020 Aishwareeya Rath

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import csv
import logging as log
import sys
from pathlib import Path

log_format = ("[%(asctime)s] {%(module)s - "
              "L:%(lineno)d} [%(levelname)s] - %(message)s")

log.basicConfig(
    level=log.INFO,
    format=log_format,
    datefmt="%D %H:%M:%S",
)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", help="Path to CSV file.", required=True)
    args = p.parse_args()
    return args


def load(file):
    log.info(f"Reading file: {file}")
    contents = []
    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                log.info(f"Read: {row}")
                contents.append(row)
    except Exception as e:
        log.debug(e)
        log.error("Cannot read file: {file} - Exiting...")
        sys.exit(1)
    return contents


def found(file):
    _ = Path(file)
    return _.is_file()


def read_file(file):
    load(file)


if __name__ == "__main__":
    args = parse_args()
    file = args.file

    if file == "" or not found(file):
        raise ValueError("Please provide a valid path to your CSV file.")

    read_file(file)
