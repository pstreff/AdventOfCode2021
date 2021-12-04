import numpy as np


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        inputs = [number for number in f.readline().rstrip().split(',')]
        matrices = []

        for _ in f:
            matrix = np.matrix([[line for line in f.readline().rstrip().split()] for _ in range(5)])
            matrices.append(matrix)

        return inputs, matrices


def check_columns(matrix):
    for col in [col.flatten() for col in [matrix[:, x] for x in range(5)]]:
        if np.all(col == 'X'):
            return True
        else:
            continue
    return False


def check_rows(matrix):
    for row in matrix:
        if np.all(row == 'X'):
            return True
        else:
            continue
    return False


def part1(file='input_test.txt'):
    inputs, matrices = get_input(file)

    winning_number = None

    for pull in inputs:
        winning_number = pull
        for matrix in matrices:
            matrix[matrix == pull] = 'X'

            if check_columns(matrix) or check_rows(matrix):
                # we have winner
                sum_of_numbers = matrix[matrix != 'X'].astype(np.int64).sum(axis=1)[0, 0]

                print(f'Part 1')
                print(f'Winner for number {winning_number}')
                print(f'Result {sum_of_numbers * int(winning_number)}')
                return


def part2(file='input_test.txt'):
    inputs, matrices = get_input(file)

    winning_number = None
    winning_sums = []

    for pull in inputs:
        winning_number = pull
        for matrix in matrices:
            matrix[matrix == pull] = 'X'

            if check_columns(matrix) or check_rows(matrix):
                # we have winner
                sum_of_numbers = matrix[matrix != 'X'].astype(np.int64).sum(axis=1)[0, 0]
                winning_sums.append(sum_of_numbers * int(winning_number))

        matrices = [matrix for matrix in matrices if not check_columns(matrix) and not check_rows(matrix)]
        if not matrices:
            print('Part 2')
            print(f'Last winning sum {winning_sums[-1]}')
            return


part1()
part1('input.txt')
part2()
part2('input.txt')
