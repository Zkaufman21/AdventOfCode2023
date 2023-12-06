# Zachary Kaufman
# This is for the advent of coding challenge
# 12-06-23
from functools import reduce


def runPart1():
    file = open('input.txt', 'r')
    raw_times = file.readline()
    raw_distances = file.readline()

    raw_times = raw_times.split(':')[1]
    raw_distances = raw_distances.split(':')[1]

    times = raw_times.split(' ')
    distances = raw_distances.split(' ')

    times = [int(time) for time in times if time != '']
    distances = [int(dist) for dist in distances if dist != '']

    number_of_valid_times = []
    for i in range(len(times)):
        time = times[i]
        valid_times = 0
        for possible_time in range(time):
            if possible_time * (time - possible_time) > distances[i]:
                valid_times += 1
        number_of_valid_times.append(valid_times)
    
    return reduce(lambda x, y: x * y, number_of_valid_times)


def runPart2():
    file = open('input.txt', 'r')
    raw_times = file.readline()
    raw_distances = file.readline()

    raw_times = raw_times.split(':')[1]
    raw_distances = raw_distances.split(':')[1]

    time = int(raw_times.strip().replace(' ', ''))
    distance = int(raw_distances.strip().replace(' ', ''))
    valid_times = 0
    for possible_time in range(time):
        if possible_time * (time - possible_time) > distance:
            valid_times += 1

    return valid_times


if __name__ == '__main__':
    print('\nPart 1')
    print('value: ' + str(runPart1()))
    print('\nPart 2')
    print('value: ' + str(runPart2()))
