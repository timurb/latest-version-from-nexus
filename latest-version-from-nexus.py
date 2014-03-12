#!/usr/bin/env python

import sys

from argparse import ArgumentParser
from argparse import FileType
from lxml import etree
from pkg_resources import parse_version

parser = ArgumentParser(description="This program extracts latest version of artifact from provided maven-metadata.xml")

parser.add_argument("file", type=FileType('r'), help="Path to maven-metadata.xml")
args = parser.parse_args()

try:
    tree = etree.parse(args.file)
except etree.XMLSyntaxError as e:
    print("Error in XML file: " + e.message)
    exit(1)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

versions = tree.xpath('/metadata/versioning/versions/version')
versions = (version.text for version in versions)
versions = map(str, versions)

print sorted(versions, key=parse_version)[-1]