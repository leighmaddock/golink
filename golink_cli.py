#!/usr/bin/env python
from golink import golink
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--link", help="URI to redirect")
parser.add_argument("--linkto", help="URL to redirect to")
parser.add_argument("--method", help="Add, Remove or fetch a URL", choices=["add", "remove", "fetch"], required=True)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()

golinkobj = golink()

if args.method == "add":
    if not args.link or not args.linkto:
        print "Add requires link and linkto"
        parser.print_help()
    golinkobj.add(args.link, args.linkto)

elif args.method == "remove":
    if not args.link:
        print "Remove requires link"
        parser.print_help()
    golinkobj.remove(args.link)

elif args.method == "fetch":
    if not args.link:
        print "Fetch requires link"
        parser.print_help()
    linkto = golinkobj.fetch(args.link)
    if not linkto:
        print "Link {0} not found".format(args.link)
        exit(1)
    print linkto
