from rmlaparse import aparser
import sys


def run():
    filename = sys.args[1]
    ap = aparser.ApacheParse(filename)
    for one_record in ap.record_dicts():
        print(one_record)
