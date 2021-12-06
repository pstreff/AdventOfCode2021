from collections import deque


def get_input(file):
    with open(file, 'r') as f:
        return [int(x) for x in f.read().split(',')]


def part1(file='input_test.txt', evolutions=80):
    input_data = get_input(file)

    fishes = deque([input_data.count(i) for i in range(9)])

    for _ in range(evolutions):
        inc = fishes[0]
        fishes.rotate(-1)
        fishes[6] += inc

    print(f'---- Evolution {evolutions} ----')
    print(fishes)
    print(sum(fishes))


part1(evolutions=80)
part1(file='input.txt', evolutions=80)
print('Part 2')
part1(evolutions=256)
part1(file='input.txt', evolutions=256)
