#!/usr/bin/env python3

# Copyright © 2020 Andrea Giacobino <no.andrea@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse


# Commands

def cmd_massage(args):
    """
    Massage the dataset
    """
    pass


def cmd_serve(args):
    """
    Serve the api
    """
    pass


def main():
    commands = [
        {
            'name': 'massage',
            'help': 'parse a csv dataset into a json one',
            'target': cmd_massage,
            'opts': [
                {
                    "names": ["--in"],
                    "help": "csv input file",
                    "default": "data.csv"
                },
                {
                    "names": ["--out"],
                    "help": "json output file",
                    "default": "data.json"
                }
            ]
        },
        {
            'name': 'serve',
            'help': 'serve the dataset from a json file',
            'target': cmd_serve,
            'opts': [
                {
                    "names": ["--data"],
                    "help": "the json dataset to serve",
                    "default": "data.json"
                }
            ]
        },
    ]
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.required = True
    subparsers.dest = 'command'
    # register all the commands
    for c in commands:
        subparser = subparsers.add_parser(c['name'], help=c['help'])
        subparser.set_defaults(func=c['target'])
        # add the sub arguments
        for sa in c.get('opts', []):
            subparser.add_argument(*sa['names'],
                                   help=sa['help'],
                                   action=sa.get('action'),
                                   default=sa.get('default'))

    # parse the arguments
    args = parser.parse_args()
    # call the function
    args.func(args)


if __name__ == "__main__":
    main()
