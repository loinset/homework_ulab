import math

IP_FIRST_CONST = 256


def int32_to_ip(number):
    power = 3
    put_ip = ""
    while power:
        cell_power = pow(IP_FIRST_CONST, power)
        middle_value = (number // cell_power) % 256
        # "% 256" if someone enters a number greater than what IPv4 can hold
        number -= middle_value * cell_power
        put_ip += str(middle_value) + '.'
        power -= 1
    put_ip += str(number % 256)  # "% 256" if someone enters a number greater than what IPv4 can hold
    return put_ip


enter_number = int(input())
print(int32_to_ip(enter_number))
