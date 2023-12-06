# Zachary Kaufman
# This is for the advent of coding challenge
# 12-05-23

def runPart1():
    file = open('input.txt', 'r')
    seed_line = file.readline()
    seed_line = seed_line.strip()
    seeds_string = seed_line.split(':')
    seeds = seeds_string[1].split(' ')
    seeds = [int(seed) for seed in seeds if seed != '']

    maps = {"seed-to-seed": {seed: seed for seed in seeds}}
    last_map = "seed-to-seed"
    current_map = None
    for line in file:
        if line == '\n':
            continue
        if not line[0].isdigit():
            if current_map is not None:
                for prev_mapped_val in maps[last_map].values():
                    if prev_mapped_val not in maps[current_map].keys():
                        maps[current_map][prev_mapped_val] = prev_mapped_val
            last_map = current_map if current_map is not None else last_map
            current_map = line.split(':')[0].split(' ')[0]
            maps[current_map] = {}
        else:
            values = line.split(' ')
            dest_start, source_start, range_val = int(values[0]), int(values[1]), int(values[2])
            source_end = source_start + range_val - 1
            for prev_mapped_val in maps[last_map].values():
                if source_start <= prev_mapped_val <= source_end:
                    maps[current_map][prev_mapped_val] = dest_start + (prev_mapped_val - source_start)

    for prev_mapped_val in maps[last_map].values():
        if prev_mapped_val not in maps[current_map].keys():
            maps[current_map][prev_mapped_val] = prev_mapped_val
    return min(maps["humidity-to-location"].values())


def runPart2():
    file = open('test.txt', 'r')
    return -1


if __name__ == '__main__':
    print('\nPart 1')
    print('value: ' + str(runPart1()))
    print('\nPart 2')
    print('value: ' + str(runPart2()))
