# Zachary Kaufman
# This is for the advent of coding challenge
# 12-04-23

def runPart1():
    file = open('input.txt', 'r')
    sum = 0
    for line in file:
        card_split = line.split(':')
        card_split[1] = card_split[1].replace('\n', '')
        win_vs_your_split = card_split[1].split('|')
        win_numbers = win_vs_your_split[0].split(' ')
        your_numbers = win_vs_your_split[1].split(' ')

        win_numbers = [value for value in win_numbers if value != '']
        your_numbers = [value for value in your_numbers if value != '']

        total_win_numbers = 0
        for num in your_numbers:
            if num in win_numbers:
                total_win_numbers += 1
        if total_win_numbers != 0:
            sum += pow(2, total_win_numbers-1)

    return sum


def runPart2():
    file = open('input.txt', 'r')
    cardValuesMap = {}
    for line in file:
        card_split = line.split(':')
        card_split[1] = card_split[1].replace('\n', '')
        card_id = int(card_split[0].split(' ')[-1])
        cardValuesMap[card_id] = cardValuesMap.get(card_id, 0) + 1
        win_vs_your_split = card_split[1].split('|')
        win_numbers = win_vs_your_split[0].split(' ')
        your_numbers = win_vs_your_split[1].split(' ')

        win_numbers = [value for value in win_numbers if value != '']
        your_numbers = [value for value in your_numbers if value != '']

        total_win_numbers = 0
        for num in your_numbers:
            if num in win_numbers:
                total_win_numbers += 1
        for num in range(total_win_numbers+1):
            if num != 0:
                cardValuesMap[card_id + num] = cardValuesMap.get(card_id+num, 0) + cardValuesMap.get(card_id, 0)

    return sum(cardValuesMap.values())


if __name__ == '__main__':
    print('\nPart 1')
    print('value: ' + str(runPart1()))
    print('\nPart 2')
    print('value: ' + str(runPart2()))
