#!/usr/bin/python3
"""Log parsing module"""

import re
import sys


def output(status_dict, file_size):
    """Output the metric"""
    print("File size: {}".format(file_size))
    for (key, value) in sorted(status_dict.items(), key=lambda item: item[0]):
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_counter = 0
    status_dict = {}
    file_size = 0
    try:
        for line in sys.stdin:
            pattern = re.compile(
                r".+ ?- ?\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] \"GET /projects/260 HTTP/1.1\" (.*) (\d+)"  # nopep8
            )
            line = line.strip()
            match = pattern.fullmatch(line)
            if match:
                print(match)
                status, size = match.group(1), match.group(2)
                file_size += int(size)
                line_counter += 1

                if status.isdecimal() and int(status) in codes:
                    status_count = status_dict.get(status)
                    if status_count:
                        status_dict[status] = status_count + 1
                    else:
                        status_dict[status] = 1

                if line_counter % 10 == 0:
                    output(status_dict, file_size)
    finally:
        output(status_dict, file_size)
