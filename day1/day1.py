

def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [int(line) for line in f.read().splitlines()]


def count_increases(measurements: list) -> int:
    previous_measurement = None
    increases = 0

    for measurement in measurements:
        if not previous_measurement:
            previous_measurement = measurement
            continue

        if measurement > previous_measurement:
            increases += 1

        previous_measurement = measurement

    return increases


def part1(file='input_test.txt'):
    input_data = get_input(file)

    print(count_increases(input_data))


def part2(file='input_test.txt'):
    input_data = get_input(file)

    measurements = [sum(input_data[x:x+3]) for x in range(len(input_data) - 2)]

    print(count_increases(measurements))


part1()
part1('input.txt')
part2()
part2('input.txt')
