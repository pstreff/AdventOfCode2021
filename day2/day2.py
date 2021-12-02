

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [[value[0], int(value[1])] for value in (line.split(' ') for line in f.read().splitlines())]


def part1(file='input_test.txt'):
    input_data = get_input(file)

    horizontal = depth = 0

    for direction, amount in input_data:
        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'down':
            depth += amount
        else:
            print(f'Encountered non handled direction {direction}')

    print(
        f'PART 1\n'
        f'Horizontal: {horizontal}\n'
        f'Depth: {depth}\n'
        f'Result: {horizontal*depth}\n'
        f'-------------------'
    )


def part2(file='input_test.txt'):
    input_data = get_input(file)

    horizontal = depth = aim = 0

    for direction, amount in input_data:
        if direction == 'forward':
            horizontal += amount
            depth += aim * amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount
        else:
            print(f'Encountered non handled direction {direction}')

    print(
        f'PART 2\n'
        f'Horizontal: {horizontal}\n'
        f'Depth: {depth}\n'
        f'Result: {horizontal * depth}\n'
        f'-------------------'
    )


part1()
part1('input.txt')
part2()
part2('input.txt')
