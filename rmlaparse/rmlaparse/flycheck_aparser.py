import csv


class ApacheParse:
    _RECORD_FIELDS = ['ip_address', 'auth_info1', 'auth_info2',
                      'timestamp_main_part', 'timestamp_tz', 'request',
                      'response_code', 'bytes_returned', 'referrer',
                      'user_agent']

    def __init__(self, filename):
        self.f = open(filename)

    def parse_file(self):
        r = csv.reader(self.f, delimiter=' ')
        for one_line in r:
            yield one_line


    def record_dicts(self):
        