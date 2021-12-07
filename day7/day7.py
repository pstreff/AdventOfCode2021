import numpy as np


def get_input(file):
    with open(file) as f:
        return [int(x) for x in f.read().split(',')]


def part1(file='input_test.txt'):
    input_data = get_input(file)
    input_data.sort()
    median = int(np.median(input_data))
    fuel = 0
    for crab in input_data:
        fuel += abs(crab - median)

    print(f'Fuel usage {fuel}')


def part2(file='input_test.txt'):
    input_data = get_input(file)
    input_data.sort()
    mean = int(np.mean(input_data).round())
    fuels = []
    # we try mean - 1, mean and mean + 1
    for mean in range(mean - 1, mean+2):
        fuel = 0
        for crab in input_data:
            delta = abs(crab - mean)
            fuel += (delta * (delta + 1)) / 2  # use the triangular number to get the fuel usage
        fuels.append(fuel)
    # the min value of fuels will be our solution
    print(f'Fuel usage {int(min(fuels))}')


part1()
part1('input.txt')
part2()
part2('input.txt')
