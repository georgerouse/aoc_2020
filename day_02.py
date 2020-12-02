from collections import Counter

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_02.txt') as f:
        file_data = f.read()
    input_list = [tuple(x.replace(':', '').split(' ')) for x in file_data.split('\n')]

    # Part 1
    number_of_valid_passwords = 0
    for occurances, letter, password in input_list:
        min_occurances = int(occurances.split('-')[0])
        max_occurances = int(occurances.split('-')[1])
        counter = Counter(password)
        if counter[letter] >= min_occurances and counter[letter] <= max_occurances:
            number_of_valid_passwords += 1
    print(f"Answer to part 1: {number_of_valid_passwords}")

    # Part 2
    number_of_valid_passwords = 0
    for positions, letter, password in input_list:
        first_pos = int(positions.split('-')[0])
        second_pos = int(positions.split('-')[1])

        if first_pos <= len(password):
            first_letter = password[first_pos - 1]
        else:
            first_letter = None

        if second_pos <= len(password):
            second_letter = password[second_pos - 1]
        else:
            second_letter = None

        if first_letter == letter and not second_letter == letter:
            number_of_valid_passwords += 1
        if not first_letter == letter and second_letter == letter:
            number_of_valid_passwords += 1

    print(f"Answer to part 2: {number_of_valid_passwords}")
