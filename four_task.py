import math

NAME = 'banana'


def bananas(line):
    min_limit = '1' + '0' * len(line)
    number = int(min_limit, 2) + 1
    out_set = set()

    while str(bin(number))[2:] != min_limit + '0':
        number_of_string = str(bin(number))[3:]
        checking_string = ''
        middle_string = ''
        for i in range(len(str(bin(number))[3:])):
            checking_string += line[i] * (number_of_string[i] == '1')
            middle_string += line[i] if number_of_string[i] == '1' else '-'
        if checking_string == NAME:
            out_set.add(middle_string)
        number += 1
    return out_set


enter_line = input()
