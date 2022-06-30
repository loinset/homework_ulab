import math


def zeros(number):
    power = 1
    fives_counter = [0] * 101
    # 102 for the correct iteration of a cycle of size 100 from 1 to 100
    while power < number:
        if pow(5, power) > number:
            break
        power += 1
    power -= 1
    counter = power
    while power:
        fives_counter[power] = number // pow(5, power)
        power -= 1
    result = 0
    while counter:
        result += fives_counter[counter]
        counter -= 1
    return result


enter_number = int(input())
print(zeros(enter_number))
