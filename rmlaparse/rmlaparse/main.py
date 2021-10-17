import aparser


def run():
    ap = aparser.ApacheParse(
        '/Users/reuven/Courses/Current/lerner-2021-10oct-17/rmlaparse/tests/access.log.1')
    for one_record in ap.record_dicts():
        print(one_record)


if __name__ == '__main__':
    run()
