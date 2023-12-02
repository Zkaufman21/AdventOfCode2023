# Zachary Kaufman
# This is for the advent of coding challenge
# 12-01-23
import re

from constants import *
from run_config import *


def get_first_last_including_string(line: str) -> (chr, chr):
    possible_string_reps = LIST_OF_SPELLED_DIGITS_MAP.keys()
    line = line.strip()

    first_match = re.search(r'\d', line)
    first_index = first_match.start()
    first_value = line[first_index]

    rev_line = line[::-1]
    last_match = re.search(r'\d', rev_line)
    last_index = len(line) - (last_match.start() + 1)
    last_value = line[last_index]

    for key in possible_string_reps:
        first_find_ind = line.find(key)
        last_find_ind = line.rfind(key)
        if first_find_ind == -1:
            continue
        if first_find_ind < first_index:
            first_index = first_find_ind
            first_value = LIST_OF_SPELLED_DIGITS_MAP[key]
        if last_find_ind > last_index:
            last_index = last_find_ind
            last_value = LIST_OF_SPELLED_DIGITS_MAP[key]


    return first_value, last_value


def get_first_int(line: str) -> chr:
    for char in line:
        if char.isdigit():
            return char
    return -1


def get_sum_of_values_from_input(file, include_spelled_digts: bool) -> int:
    sum = 0
    for line in file:
        if not include_spelled_digts:
            first_val = get_first_int(line)
            reversed_line = line[::-1]
            final_val = get_first_int(reversed_line)
        else:
            first_val, final_val = get_first_last_including_string(line)

        if first_val == -1 or final_val == -1:
            print("No Int Found")
            return -1
        else:
            sum += int(first_val + final_val)

    return sum


def run():
    file = open(TEST_INPUT_FILE if USE_TEST_INPUT else INPUT_FILE, "r")
    value = get_sum_of_values_from_input(file, not IS_PART_1)

    print("\nPart " + ("1" if IS_PART_1 else "2"))
    print("Sum: " + str(value))


if __name__ == '__main__':
    run()
