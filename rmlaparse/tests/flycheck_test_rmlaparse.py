import pytest
from rmlaparse import __version__
from rmlaparse.aparser import ApacheParse


def test_version():
    assert __version__ == '0.1.0'


# create a fixture with an instance of ApacheParse
@pytest.fixture
def apache_parser():
    return ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')


def test_create_instance(apache_parser):
    ap = apache_parser
    assert isinstance(ap, ApacheParse)

    # should get back a generator
    g = ap.parse_file()
    assert hasattr(g, '__iter__')
    assert hasattr(g, '__next__')


def test_parse_file_returns_list_of_strings(apache_parser):
    ap = apache_parser

    # get a list from the generator that ap.parse_file() returns
    all_records = list(ap.parse_file())

    # are all of the returned values in all_records lists?
    assert all(isinstance(one_record, list)
               for one_record in all_records)

    # are all of the fields in our first record (and presumably all of them) strings?
    first_record = all_records[0]
    assert all(isinstance(one_field, str)
               for one_field in first_record)


def test_parse_dicts(apache_parser):
    ap = apache_parser

    all_records = list(ap.record_dicts())
    assert all(isinstance(one_record, dict)
               for one_record in all_records)

    first_record = all_records[0]
    assert first_record['ip_address'] == '95.88.94.48'
