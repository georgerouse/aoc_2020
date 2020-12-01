if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_01_input.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split('\n')]

    # Part 1
    found = False
    for i, first_value in enumerate(input_list):
        for j, second_value in enumerate(input_list):
            if i == j:
                continue
            elif first_value + second_value == 2020:
                print(f"Answer to part 1: {first_value * second_value}")
                found = True
                break
        if found:
            break

    # Part 2
    from itertools import combinations
    all_3_combinations = list(combinations(input_list, 3))
    for x, y, z in all_3_combinations:
        if x + y + z == 2020:
            print(f"Answer to part 2: {x * y * z}")
            break