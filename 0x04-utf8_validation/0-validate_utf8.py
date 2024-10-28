#!/usr/bin/python3
"""Validate a UTF-8 encoding"""


def validUTF8(data):
    """The check function"""
    NEW_CHAR = 0
    FEACHING_CHAR = 1
    state = NEW_CHAR
    char_bytes_count = 0
    char_byte_index = 0
    for char in data:
        if state == NEW_CHAR:
            if (char & 0x80) == 0:
                char_bytes_count = 1
            elif (char & 0b11100000) == 0b11000000:
                char_bytes_count = 2
            elif (char & 0b11110000) == 0b11100000:
                char_bytes_count = 3
            elif (char & 0b11111000) == 0b11110000:
                char_bytes_count = 4
            else:
                # byte selection is not right
                return False
            char_byte_index = 0
            state = FEACHING_CHAR
        elif state == FEACHING_CHAR:
            if char_bytes_count == 1:
                # there is no check for the one byte char
                state = NEW_CHAR
                pass
            else:
                # for the multi byte chars each char should be
                # a continuation byte
                if char_byte_index < char_bytes_count - 1:
                    # check for the continuation byte
                    if (char & 0b11000000) != 0b10000000:
                        return False
                    char_byte_index += 1
                else:
                    state = NEW_CHAR
    return True
