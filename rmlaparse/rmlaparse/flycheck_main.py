from rmlaparse import aparser
import sys


def run():
    filename = sys.args[1]
    ap = aparser.ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')
    for one_record in ap.record_dicts():
        print(one_record)
