def run_program(command_list):
    index_list = []
    accumulator = 0
    index_tracker = 0
    while True:
        if index_tracker in index_list:
            success = False
            break
        if index_tracker == len(command_list):
            success = True
            break

        command_string, value = command_list[index_tracker]
        index_list.append(index_tracker)

        if command_string == 'acc':
            accumulator += value
            index_tracker += 1

        elif command_string == 'nop':
            index_tracker += 1

        elif command_string == 'jmp':
            index_tracker = index_tracker + value
    return success, accumulator


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_08.txt') as f:
        file_data = f.read()
    lines = file_data.split('\n')
    command_list = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

    # Part 1
    success, accumulator = run_program(command_list)
    print(f'Answer to part 1: {accumulator}')

    # Part 2
    list_possible_commands = []
    for i, (command_string, value) in enumerate(command_list):
        if command_string == 'nop':
            new_command_list = command_list.copy()
            new_command_list[i] = ('jmp', value)
            list_possible_commands.append(new_command_list)
        elif command_string == 'jmp':
            new_command_list = command_list.copy()
            new_command_list[i] = ('nop', value)
            list_possible_commands.append(new_command_list)

    for possible_command_list in list_possible_commands:
        success, accumulator = run_program(possible_command_list)
        if success:
            print(f'Answer to part 2: {accumulator}')
            break
