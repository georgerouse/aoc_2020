INPUT = [20, 0, 1, 11, 6, 3]

if __name__ == '__main__':
    number_of_turns = [(2020, 1), (30000000, 2)]
    for number_of_turns, question_number in number_of_turns:
        input_list = INPUT
        said_numbers = {}
        last_said_number = None
        last_said_number_first_time_seen = True
        debug = False

        for i in range(0, number_of_turns):
            if i + 1 <= len(input_list):
                number = input_list[i]
                last_said_number = number
                if number not in said_numbers.keys():
                    said_numbers[number] = [i+1]
            else:
                if len(said_numbers[last_said_number]) == 1:
                    last_said_number = 0
                    if last_said_number not in said_numbers.keys():
                        said_numbers[last_said_number] = [i+1]
                    else:
                        number_values = said_numbers[last_said_number]
                        number_values.append(i+1)
                        said_numbers[last_said_number] = number_values
                else:
                    last_said_turn = said_numbers[last_said_number][-1]
                    last_said_turn_before = said_numbers[last_said_number][-2]
                    number = last_said_turn - last_said_turn_before

                    last_said_number = number
                    if last_said_number not in said_numbers.keys():
                        said_numbers[last_said_number] = [i+1]
                    else:
                        number_values = said_numbers[last_said_number]
                        number_values.append(i+1)
                        said_numbers[last_said_number] = number_values
            if debug:
                print(f'Turn {i+1}: {last_said_number}')
        print(f'Answer to part {question_number}: {last_said_number}')
