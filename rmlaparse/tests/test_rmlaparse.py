from rmlaparse import __version__
from rmlaparse.aparser import ApacheParse


def test_version():
    assert __version__ == '0.1.0'


def test_create_instance():
    ap = ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')
    assert isinstance(ap, ApacheParse)

    # should get back a generator
    g = ap.parse_file()
    assert hasattr(g, '__iter__')
    assert hasattr(g, '__next__')


def test_parse_file_returns_list_of_strings():
    ap = ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')
    assert isinstance(ap, ApacheParse)

    all_records = list(ap.parse_file())

    assert all(isinstance(one_record, list)
               for one_record in all_records)

    first_record = all_records[0]
    assert all(isinstance(one_field, str)
               for one_field in first_record)
