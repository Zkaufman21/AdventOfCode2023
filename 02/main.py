# Zachary Kaufman
# This is for the advent of coding challenge
# 12-02-23
import numpy as np

checkMap = {'green': 13, 'red': 12, 'blue': 14}

def checkForValid(line: str):
    line = line.strip()
    s1 = line.split(":")
    id = s1[0].split(' ')[1]

    selections = s1[1]
    selections = selections.split(';')
    for selection in selections:
        colors = selection.split(',')
        for color in colors:
            color_name = color.split(' ')
            if int(color_name[1]) > int(checkMap[color_name[2]]):
                return 0
    return int(id)


def runPart1():
    sum = 0
    file = open('./input.txt', "r")
    for line in file:
        sum += checkForValid(line)

    return sum


def get_min(line: str):
    line = line.strip()
    s1 = line.split(":")
    map = {'red': 0, 'blue': 0, 'green': 0}
    games = s1[1]
    games = games.split(';')
    for game in games:
        colors = game.split(',')
        for color in colors:
            color_name = color.split(' ')
            if int(color_name[1]) > int(map[color_name[2]]):
                map[color_name[2]] = int(color_name[1])
    return map['red']*map['blue']*map['green']


def runPart2():
    sum = 0
    file = open('./input.txt', "r")
    for line in file:
        sum += get_min(line)

    return sum


    return None
if __name__ == '__main__':
    part1Val = runPart1()
    part2Val = runPart2()

    print("\nPart 1")
    print("Value: " + str(part1Val))
    print("Part 2")
    print("Value: " + str(part2Val))
