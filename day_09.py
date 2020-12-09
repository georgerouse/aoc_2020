from itertools import combinations

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_09.txt') as f:
        file_data = f.read()
    lines = [int(x) for x in file_data.split('\n')]

    # Part 1
    read_length = 25
    start_index = 0
    lines[0:25]
    at_the_end = False
    while True:
        numbers = lines[start_index:start_index+read_length]
        if start_index + read_length + 1 >= len(lines):
            break
        combination_list = [x for x in combinations(numbers, 2)]
        next_number = lines[start_index+read_length]
        sum_combinations = [x[0] + x[1] for x in combination_list]
        if next_number not in sum_combinations:
            print(f'Answer to part 1: {next_number}')
            break
        start_index += 1

    # Part 2
    number_to_seek = next_number
    start_index = 0
    answer_not_found = True
    while answer_not_found:
        sum = 0
        for i in range(start_index, len(lines)):
            end_index = i
            sum += lines[i]
            if sum == number_to_seek:
                answer_not_found = False
                break
            if sum > number_to_seek:
                start_index += 1
                break
        if start_index == len(lines):
            break

    smallest_number = min(lines[start_index:end_index+1])
    largest_number = max(lines[start_index:end_index+1])
    print(f'Answer to part 2: {smallest_number+largest_number}')
