#!python
# tribe-admin
# Administrative utility for working with Tribe data
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 13 14:08:12 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: tribe-admin.py [5232e54] benjamin@bengfort.com $

"""
Administrative utility for working with Tribe data
"""

##########################################################################
## Imports
##########################################################################

import sys
import json
import tribe
import argparse
import networkx as nx

from tribe.utils import timeit
from tribe.utils import humanizedelta
from tribe.viz import draw_social_network
from tribe.extract import ConsoleMBoxReader as MBoxReader

##########################################################################
## Command Variables
##########################################################################

DESCRIPTION = "An administrative utility for the Tribe Social Network Analysis"
EPILOG      = "If there are any bugs or concerns, submit an issue on Github"
VERSION     = "tribe v{}".format(tribe.__version__)

##########################################################################
## Commands
##########################################################################

def header_analysis(args):
    """
    Perform a header analysis on an MBox
    """

    @timeit
    def timed_inner(path):
        reader  = MBoxReader(path)
        return reader.header_analysis()

    headers, seconds = timed_inner(args.mbox[0])

    if args.show:
        headers.plot()

    json.dump(headers, args.write)
    return "Analysis complete in {}".format(humanizedelta(seconds=seconds))


def count_emails(args):
    """
    Count the number of emails in an MBox.
    """

    @timeit
    def timed_inner(path):
        reader = MBoxReader(path)
        return reader.count()

    count, seconds = timed_inner(args.mbox[0])
    elapsed = humanizedelta(seconds=seconds)
    return "Found {:,} emails in {}".format(count, elapsed)


def extract(args):
    """
    Extract a GraphML file from an MBox
    """

    @timeit
    def timed_inner(path, outpath):
        reader = MBoxReader(path)
        G = reader.extract_graph()
        nx.write_graphml(G, outpath)
        return reader.errors

    print("Starting Graph extraction, a long running process")
    errors, seconds = timed_inner(args.mbox[0], args.write)
    print("GraphML written out to {}".format(args.write.name))

    if errors:
        print("\nThe following errors were encountered:")
        for err, num in errors.most_common():
            print("    {}: {}".format(num, err))
        print("\n")
    else:
        print("\nNo errors encountered in processing\n")

    return "Graph extraction took {}".format(humanizedelta(seconds=seconds))


def info(args):
    """
    Print information about a GraphML file
    """
    for idx, path in enumerate(args.graphml):
        G = nx.read_graphml(path)
        print(nx.info(G))

        if idx < len(args.graphml) - 1:
            print("----")

    return ""


def draw(args):
    """
    Draw a GraphML with the tribe draw method.
    """
    G = nx.read_graphml(args.graphml[0])
    draw_social_network(G, args.write)
    return ""


##########################################################################
## Main Function and Methodology
##########################################################################

def main(*args):

    # Construct the argument parser
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    subparsers = parser.add_subparsers(title='commands', description='Administrative commands for Tribe')

    # Version Command
    parser.add_argument('-v', '--version', action='version', version=VERSION)

    # Headers Analysis Command
    headers_parser = subparsers.add_parser('headers', help='Perform an analysis of the email headers in an MBox')
    headers_parser.add_argument('-w', '--write', type=argparse.FileType('w'), default=sys.stdout, help='Location to write data to')
    headers_parser.add_argument('-s', '--show', action='store_true', default=False, help='Show graph of key distribution')
    headers_parser.add_argument('mbox', type=str, nargs=1, help='Path or location to MBox for analysis')
    headers_parser.set_defaults(func=header_analysis)

    # Count Emails Command
    count_parser = subparsers.add_parser('count', help='Count the number of emails in an MBox.')
    count_parser.add_argument('mbox', type=str, nargs=1, help='Path or location to MBox for analysis')
    count_parser.set_defaults(func=count_emails)

    # Extract Command
    extract_parser = subparsers.add_parser('extract', help='Extract a GraphML file from an MBox')
    extract_parser.add_argument('-w', '--write', type=argparse.FileType('wb'), default=sys.stdout, help='Location to write data to')
    extract_parser.add_argument('mbox', type=str, nargs=1, help='Path or location to MBox for analysis')
    extract_parser.set_defaults(func=extract)

    # Graph Info Command
    info_parser = subparsers.add_parser('info', help='Print information about a GraphML file')
    info_parser.add_argument('graphml', nargs="+", type=argparse.FileType('r'), help='Location of MBox(es) to get info for')
    info_parser.set_defaults(func=info)

    # Draw Command
    draw_parser = subparsers.add_parser('draw', help='Draw a GraphML using the tribe draw method')
    draw_parser.add_argument('-w', '--write', type=str, default=None, help='Location to draw to')
    draw_parser.add_argument('graphml', nargs=1, type=argparse.FileType('r'), help='Location of GraphML to draw')
    draw_parser.set_defaults(func=draw)

    # Handle input from the command line
    args = parser.parse_args()            # Parse the arguments
    try:
        msg = args.func(args)             # Call the default function
        parser.exit(0, msg+"\n")               # Exit cleanly with message
    except Exception as e:
        parser.error(str(e))              # Exit with error

if __name__ == '__main__':
    main(*sys.argv[1:])
