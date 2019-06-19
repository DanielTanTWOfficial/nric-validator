import random

def first_char(val):
    switch = {
        0: 'S',
        1: 'T',
        2: 'F',
        3: 'G'
    }
    return switch.get(val)


def last_char1(val):
    switch = {
        0: 'J',
        1: 'Z',
        2: 'I',
        3: 'H',
        4: 'G',
        5: 'F',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A'
    }
    return switch.get(val)


def last_char2(val):
    switch = {
        0: 'X',
        1: 'W',
        2: 'U',
        3: 'T',
        4: 'R',
        5: 'Q',
        6: 'P',
        7: 'N',
        8: 'M',
        9: 'L',
        10: 'K'
    }
    return switch.get(val)


def main():
    # this script generates random valid nric numbers
    nric = []

    # generate a random 1st letter
    a = first_char(random.randint(0,3))
    nric.append(a)

    for i in range(7):
        nric.append(random.randint(0,9))

    x = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

    if nric[0] == 'T' or nric[0] == 'G':
        x = x + 4

    y = x % 11

    if nric[0] == 'S' or nric[0] == 'T':
        nric.append(last_char1(y))
    elif nric[0] == 'F' or nric[0] == 'G':
        nric.append(last_char2(y))

    print('nric: ' + ''.join(map(str,nric)) + '\n')

main()
