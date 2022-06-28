import math


def zeros(number):
    counter = 0
    for i in range(number + 1):
        power = 1
        middle_counter = 0
        while pow(5, power) <= i:
            if i % pow(5, power) == 0:
                middle_counter = power
            else:
                break
            power += 1
        counter += middle_counter
    return counter


enter_number = int(input())
print(zeros(enter_number))
