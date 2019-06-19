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


def validate_num(nric):
    x = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

    if nric[0] == 'T' or nric[0] == 'G':
        x = x + 4

    y = x % 11

    if nric[0] == 'S' or nric[0] == 'T':
        z = last_char1(y)

        if nric[8] == z:
            return True
        else:
            return False
    elif nric[0] == 'F' or nric[0] == 'G':
        z = last_char2(y)

        if nric[8] == z:
            return True
        else:
            return False


def permgen(items, n):
    # generates the 1st 4 numbers of nric
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permgen(items,n-1):
                yield [items[i]]+cc


def construct_ic(val):
    for c in permgen(['0','1','2','3','4','5','6','7','8','9'],4):
        for i in range(4):
            nric = []
            if i == 0:
                nric.append('S')
                nric.append(''.join(c))
                nric.append(val)
                
                # try nric
                success = validate_num(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            elif i == 1:
                nric.append('T')
                nric.append(''.join(c))
                nric.append(val)

                success = validate_num(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            elif i == 2:
                nric.append('F')
                nric.append(''.join(c))
                nric.append(val)

                success = validate_num(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()
            else:
                nric.append('G')
                nric.append(''.join(c))
                nric.append(val)

                success = validate_num(''.join(nric))

                if success:
                    f = open('nric.txt', 'a')
                    f.write(''.join(nric) + '\n')
                    f.close()


def main():
    # get user input
    val = input('Enter last 4 characters of nric: ')

    construct_ic(val)

main()
