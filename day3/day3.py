from collections import defaultdict


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [line for line in f.read().splitlines()]


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
    print(f'Gamma {gamma}')
    print(f'Epsilon {epsilon}')
    print(f'Result {gamma * epsilon}')


part1()
part1('input.txt')