from rmlaparse.aparser import ApacheParse
from rmlaparse import __version__
import pytest


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def apache_parser():
    log = ApacheParse('tests/access.log.1')
    print(log)
    return log


def test_create_instance(apache_parser):
    ap = apache_parser
    assert isinstance(ap, ApacheParse)
    g = ap.parse_file()
    assert hasattr(g, '__iter__')
    assert hasattr(g, '__next__')


def test_returns_list_of_strings():
    ap = apache_parser
    all_records = list(ap.parse_file())
    assert all(isinstance(one_record, list)
               for one_record in all_records)
    first_record = all_records[0]
    assert all(isinstance(one_field, str)
               for one_field in first_record)


def test_returns_dict():
    ap = apache_parser
    all_records = list(ap.record_dicts())
    assert all(isinstance(one_record, dict)
               for one_record in all_records)
