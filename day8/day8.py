from itertools import permutations


def get_input(file):
    with open(file) as f:
        return [line.split() for line in [line for line in f.read().splitlines()]]


def part1(file='input_test.txt'):
    input_data = get_input(file)
    easy_numbers_len = [2, 3, 4, 7]
    easy_numbers = 0
    for x in input_data:
        for y in x[x.index('|'):]:
            easy_numbers += 1 if len(y) in easy_numbers_len else 0

    print(easy_numbers)
    pass


def identify_easy_numbers(data):
    numbers = {}
    for number in data:
        if number == '|':
            continue
        if len(number) == 2:
            numbers[1] = number
        elif len(number) == 3:
            numbers[7] = number
        elif len(number) == 4:
            numbers[4] = number
        elif len(number) == 7:
            numbers[8] = number
        else:
            continue

    return numbers


def identify_len_six_numbers(numbers, data):
    for number in data:
        if number == '|' or len(number) != 6:
            continue
        # check for number 9
        if all([x in number for x in numbers[4]]):
            numbers[9] = number
        elif all([x in number for x in numbers[7]]):  # check for number 0
            numbers[0] = number
        else:  # it is a 6
            numbers[6] = number

    return numbers


def identify_len_five_numbers(numbers, data):
    for number in data:
        if number == '|' or len(number) != 5:
            continue
        # check for number 3
        if all([x in number for x in numbers[7]]):
            numbers[3] = number
        elif sum([x in number for x in numbers[6]]) == 5:  # check for number 5
            numbers[5] = number
        else:  # it is a 2
            numbers[2] = number

    return numbers
    pass


def decode_four_digit_output(numbers, data):
    digits = ''
    for output_digit in data[data.index('|') + 1:]:
        for number, code in numbers.items():
            if output_digit in [''.join(p) for p in permutations(code)]:
                digits += str(number)
    return int(digits)


def part2(file='input_test.txt'):
    input_data = get_input(file)
    output_sum = 0
    for x in input_data:
        numbers = identify_easy_numbers(x)
        numbers = identify_len_six_numbers(numbers, x)
        numbers = identify_len_five_numbers(numbers, x)
        output_sum += decode_four_digit_output(numbers, x)

    print(output_sum)


part1()
part1('input.txt')
part2()
part2('input.txt')
