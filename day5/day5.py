from collections import defaultdict


def get_input(file='input_test.txt'):
    with open(file, 'r') as f:
        return [
            [tuple(map(int, p1.split(','))), tuple(map(int, p2.split(',')))]
            for p1, p2 in [line.split(' -> ') for line in f.read().splitlines()]
        ]


def get_points(p1, p2):
    if p1[0] == p2[0]:  # when x1 == x2 get points where y increments
        if p1[1] < p2[1]:
            r = range(p1[1], p2[1] + 1, 1)
        else:
            r = range(p2[1], p1[1] + 1, 1)
        for y in r:
            yield p1[0], y
    elif p1[1] == p2[1]:  # when y1 == y2 get points where x increments
        if p1[0] < p2[0]:
            r = range(p1[0], p2[0] + 1, 1)
        else:
            r = range(p2[0], p1[0] + 1, 1)
        for x in r:
            yield x, p1[1]
    else:  # diagonal line
        if p1[0] < p2[0]:
            x_change = 1
        else:
            x_change = -1

        x_range = range(p1[0], p2[0] + x_change, x_change)

        if p1[1] < p2[1]:
            # slope goes down
            y_change = 1
        else:  # slope goes up
            y_change = -1

        y_range = range(p1[1], p2[1] + y_change, y_change)

        for point in zip(x_range, y_range):
            yield point


def part1(file='input_test.txt'):
    input_data = get_input(file)
    dangerous_points = defaultdict(lambda: 0)
    for p1, p2 in input_data:
        if p1[0] == p2[0] or p1[1] == p2[1]:
            for point in get_points(p1, p2):
                dangerous_points[point] += 1
    number_of_overlaps = len([v for v in dangerous_points.values() if v >= 2])
    print(f'Number of overlaps {number_of_overlaps}')


def part2(file='input_test.txt'):
    input_data = get_input(file)
    dangerous_points = defaultdict(lambda: 0)
    for p1, p2 in input_data:
        for point in get_points(p1, p2):
            dangerous_points[point] += 1
    number_of_overlaps = len([v for v in dangerous_points.values() if v >= 2])
    print(f'Number of overlaps {number_of_overlaps}')


part1()
part1('input.txt')
part2()
part2('input.txt')
