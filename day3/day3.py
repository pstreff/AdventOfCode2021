import time
from collections import defaultdict


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [line for line in f.read().splitlines()]


@timing
def part1(file='input_test.txt'):
    input_data = get_input(file)
    data = defaultdict(lambda: [0, 0])

    for bit_string in input_data:
        for index in reversed(range(len(input_data[0]))):
            bit = int(bit_string, 2) >> index & 1
            data[index][bit] += 1

    gamma = epsilon = ''

    for bit in [str(list_.index(max(list_))) for _, list_ in data.items()]:
        gamma += bit
        epsilon += str(1 - int(bit))

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print('Part 1')
    print(f'Gamma {gamma}')
    print(f'Epsilon {epsilon}')
    print(f'Result {gamma * epsilon}')


def get_bit(val, n):
    return val >> n & 1

@timing
def part1_bit_operations(file='input_test.txt'):
    with open(file, 'r') as f:
        first = f.readline().rstrip()
        bit_size = len(first)
        input_data = [int(first, 2)]
        input_data += [int(line, 2) for line in f.read().splitlines()]

    data = defaultdict(lambda: [0, 0])

    bitmask = (1 << bit_size) - 1

    for number in input_data:
        for index in reversed(range(bit_size)):
            bit = get_bit(number, index)
            data[index][bit] += 1

    gamma = int(''.join([str(list_.index(max(list_))) for _, list_ in data.items()]), 2)

    epsilon = gamma ^ bitmask

    print('Part 1 with more bit operation')
    print(f'Gamma {gamma}')
    print(f'Epsilon {epsilon}')
    print(f'Result {gamma * epsilon}')


@timing
def part2(file='input_test.txt'):
    with open(file, 'r') as f:
        first = f.readline().rstrip()
        bit_size = len(first)
        input_data = [int(first, 2)]
        input_data += [int(line, 2) for line in f.read().splitlines()]

    oxygen = input_data.copy()
    co2 = input_data.copy()
    index = bit_size - 1

    while len(oxygen) != 1 or len(co2) != 1:
        oxygen_bits = [0, 0]
        co2_bits = [0, 0]
        if len(oxygen) != 1:
            for number in oxygen:
                bit = get_bit(number, index)
                oxygen_bits[bit] += 1

            oxygen_bit_criteria = 1 if oxygen_bits[0] == oxygen_bits[1] else oxygen_bits.index(max(oxygen_bits))

            for number in oxygen.copy():
                bit = get_bit(number, index)
                if bit != oxygen_bit_criteria:
                    oxygen.remove(number)

        if len(co2) != 1:
            for number in co2:
                bit = get_bit(number, index)
                co2_bits[bit] += 1

            co2_bit_criteria = 0 if co2_bits[0] == co2_bits[1] else co2_bits.index(min(co2_bits))

            for number in co2.copy():
                bit = get_bit(number, index)
                if bit != co2_bit_criteria:
                    co2.remove(number)

        index -= 1

    oxygen = oxygen[0]
    co2 = co2[0]

    print('Part 2')
    print(f'Oxygen {oxygen}')
    print(f'CO2 {co2}')
    print(f'Result {oxygen * co2}')


@timing
def part2_experimental(file='input_test.txt'):
    with open(file, 'r') as f:
        first = f.readline().rstrip()
        bit_size = len(first)
        input_data = [int(first, 2)]
        input_data += [int(line, 2) for line in f.read().splitlines()]

    oxygen = input_data.copy()
    co2 = input_data.copy()
    index = bit_size - 1

    while len(oxygen) != 1 or len(co2) != 1:
        if len(oxygen) != 1:
            data = {
                0: [],
                1: []
            }
            for number in oxygen:
                bit = get_bit(number, index)
                data[bit].append(number)

            zero_bits = len(data[0])
            one_bits = len(data[1])

            if zero_bits == one_bits or zero_bits < one_bits:
                to_remove = 0
            else:
                to_remove = 1

            oxygen = list(set(oxygen)-set(data[to_remove]))

        if len(co2) != 1:
            data = {
                0: [],
                1: []
            }
            for number in co2:
                bit = get_bit(number, index)
                data[bit].append(number)

            zero_bits = len(data[0])
            one_bits = len(data[1])

            if zero_bits == one_bits or zero_bits < one_bits:
                to_remove = 1
            else:
                to_remove = 0

            co2 = list(set(co2)-set(data[to_remove]))

        index -= 1

    oxygen = oxygen[0]
    co2 = co2[0]

    print('Part 2 Experimental')
    print(f'Oxygen {oxygen}')
    print(f'CO2 {co2}')
    print(f'Result {oxygen * co2}')


# part1()
# print('--------------------------------')
part1('input.txt')
print('--------------------------------')
# part1_bit_operations()
# print('--------------------------------')
part1_bit_operations('input.txt')
print('--------------------------------')
# part2()
# print('--------------------------------')
part2('input.txt')
print('--------------------------------')
# part2_experimental()
# print('--------------------------------')
part2_experimental('input.txt')