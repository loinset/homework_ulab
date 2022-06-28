

def count_find_num(primes_l, limit):
    map_mass = [0] * (limit + 1)
    res = 1
    for i in primes_l:
        res *= i
    if res > limit:
        return []
    map_mass[res] = res
    counter = res
    while counter != limit:
        for i in primes_l:
            if map_mass[counter] != 0 and counter * i <= limit:
                map_mass[counter * i] = counter * i
        counter += 1
    num_list = set(map_mass)
    num_list.remove(0)
    exit_list = [len(num_list), max(num_list)]
    return exit_list


enter_primesL = list(map(lambda x: int(x), (input().replace('\n', '').split(' '))))
enter_limit = int(input())
print(count_find_num(enter_primesL, enter_limit))
