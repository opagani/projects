from rmlaparse import __version__
from rmlaparse.aparser import ApacheParse


def test_version():
    assert __version__ == '0.1.0'


def test_create_instance():
    ap = ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')
    assert isinstance(ap, ApacheParse)
    g = ap.parse_file()
    