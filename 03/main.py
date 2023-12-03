# Zachary Kaufman
# This is for the advent of coding challenge
# 12-03-23
from run_config import *

SYMBOLS = ['$', '*', '/', '=', '-', '&', '@', '+', '%', '#']
LINE_LENGTH = 140
POSITION_MODIFIER_ARRAY = [-LINE_LENGTH - 1, -LINE_LENGTH, -LINE_LENGTH + 1, -1, 1, LINE_LENGTH - 1, LINE_LENGTH,
                           LINE_LENGTH + 1]


def get_full_number_and_replace(f: str, ind: int) -> (str, int):
    num = f[ind]
    f = f[:ind:] + '.' + f[ind+1::]
    prefix = ''
    suffix = ''

    prefix_ind = ind-1
    while prefix_ind % LINE_LENGTH < LINE_LENGTH-1 and f[prefix_ind].isdigit():
        prefix += f[prefix_ind]
        f = f[:prefix_ind:] + '.' + f[prefix_ind+1::]
        prefix_ind -= 1

    prefix = prefix[::-1]

    suffix_ind = ind + 1
    while suffix_ind % LINE_LENGTH > 0 and f[suffix_ind].isdigit():
        suffix += f[suffix_ind]
        f = f[:suffix_ind:] + '.' + f[suffix_ind+1::]
        suffix_ind += 1
    return f, int(prefix+num+suffix)


def check_for_edge_cases(index, modifier, file_len) -> bool:
    if index % LINE_LENGTH == 0 and modifier in [-LINE_LENGTH - 1, -1, LINE_LENGTH - 1]:
        return True
    if index < LINE_LENGTH and modifier in [-LINE_LENGTH - 1, -LINE_LENGTH, -LINE_LENGTH + 1]:
        return True
    if index % LINE_LENGTH == LINE_LENGTH - 1 and modifier in [-LINE_LENGTH + 1, 1, LINE_LENGTH + 1]:
        return True
    if index > file_len - LINE_LENGTH and modifier in [LINE_LENGTH - 1, LINE_LENGTH, LINE_LENGTH + 1]:
        return True


def runPart1():
    file = open('./input.txt' if not USE_TEST_INPUT_FILE else './test.txt', "r")
    f = file.read()
    f = f.replace('\n', '')
    sum = 0
    file_len = len(f)
    for symb in SYMBOLS:
        indices = [i for i, x in enumerate(f) if x == symb]
        for ind in indices:
            for modifier in POSITION_MODIFIER_ARRAY:
                if check_for_edge_cases(ind, modifier, file_len):
                    continue
                if f[ind+modifier].isdigit():
                    f, new_num = get_full_number_and_replace(f, ind+modifier)
                    sum += new_num
    return sum

def runPart2():
    file = open('./input.txt' if not USE_TEST_INPUT_FILE else './test.txt', "r")
    f = file.read()
    g = f.replace('\n', '')
    sum = 0

    indices = [i for i, x in enumerate(g) if x == '*']
    file_len = len(g)
    for ind in indices:
        gear_nums = []
        for modifier in POSITION_MODIFIER_ARRAY:
            if check_for_edge_cases(ind, modifier, file_len):
                continue
            if g[ind + modifier].isdigit():
                g, new_num = get_full_number_and_replace(g, ind + modifier)
                gear_nums.append(new_num)
        if len(gear_nums) == 2:
            sum += gear_nums[0] * gear_nums[1]
    return sum


if __name__ == '__main__':
    print('\nPart 1')
    print('value: ' + str(runPart1()))
    print('\nPart 2')
    print('value: ' + str(runPart2()))
