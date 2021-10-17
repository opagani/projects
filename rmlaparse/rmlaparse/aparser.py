import csv


class ApacheParse:
    def __init__(self, filename):
        self.f = open(filename)

    def parse_file(self):
        r = csv.reader(self.f, delimiter=' ')
        for one_line in r:
            yield one_line
