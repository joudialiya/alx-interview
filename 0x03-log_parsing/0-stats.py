#!/usr/bin/python3
"""Log parsing module"""
import re
import sys
import signal

status_count_dict = dict()
line_counter = 0
totale_size = 0


def output(*args):
    """Output the metric"""
    print("File size: {}".format(totale_size))
    for (key, value) in sorted(status_count_dict.items(), key=lambda item: item[0]):
        print("{}: {}".format(key, value))


signal.signal(signal.SIGINT, output)
if __name__ == '__main__':
    for line in sys.stdin:
        pattern = re.compile(
            r"(?:\d{,3}\.?){4} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d*] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d{3})"
        )
        match = re.match(pattern, line)
        if match:
            status, size = match.groups()[0], match.groups()[1]
            status_count = status_count_dict.get(status)
            status_count_dict[status] = status_count + 1 if (status_count) else 1
            totale_size += int(size)
            line_counter += 1

            if line_counter % 10 == 0:
                output()
