from rmlaparse import __version__
from rmlaparse.aparser import ApacheParse


def test_version():
    assert __version__ == '0.1.0'


def test_create_instance():
    ap = ApacheParse('/etc/passwd')
    assert isinstance(ap, ApacheParse)
