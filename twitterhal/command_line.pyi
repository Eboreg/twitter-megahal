from argparse import ArgumentParser, Namespace, _MutuallyExclusiveGroup
from typing import Type

import twitterhal


def init_logging(loglevel: int):
    ...


def main():
    ...


class CommandLine:
    args: Namespace
    init_megahal: bool
    parser: ArgumentParser
    mutex: _MutuallyExclusiveGroup
    TwitterHAL: Type[twitterhal.TwitterHAL]
    hal: twitterhal.TwitterHAL

    def __init__(self, twitterhal_class: Type[twitterhal.TwitterHAL]):
        ...

    def print_stats(self, *args, **kwargs):
        ...

    def run(self, *args, **kwargs):
        ...

    def run_extra(self, *args, **kwargs) -> bool:
        ...

    def setup(self, *args, **kwargs):
        ...

    def __exit__(self, *args, **kwargs):
        ...

    def __enter__(self):
        ...
