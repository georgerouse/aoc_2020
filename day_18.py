from functools import reduce


def evaluate_char_list(char_list, return_type='str'):
    result = 0.0
    for i, char in enumerate(char_list):
        if i + 1 == len(char_list):
            break
        elif i == 0:
            result = int(char)
        elif char == '*':
            result *= int(char_list[i+1])
        elif char == '+':
            result += int(char_list[i+1])
    if return_type == 'str':
        return str(result)
    else:
        return result


def evaluate_char_list_v2(char_list, return_type='str'):
    plus_stack = []
    for i, char in enumerate(char_list):
        if char == '+':
            plus_stack.append((i, char))

    if plus_stack:
        while plus_stack:
            for i, plus_value in enumerate(plus_stack):
                left_val = int(char_list[plus_value[0]-1])
                right_val = int(char_list[plus_value[0]+1])
                result = f'{left_val + right_val}'
                for index in range(plus_value[0]-1, plus_value[0]+2):
                    char_list.pop(plus_value[0]-1)
                char_list.insert(plus_value[0]-1, result)
                plus_stack.pop(0)
                plus_stack = []
                for i, char in enumerate(char_list):
                    if char == '+':
                        plus_stack.append((i, char))
                break

    number_list = [int(x) for x in char_list if x != '*']
    return_value = reduce(lambda x, y: x*y, number_list)
    if return_type == 'str':
        return str(return_value)
    else:
        return return_value

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_18.txt') as f:
        file_data = f.read()
    lines = [x.replace(' ', '') for x in file_data.split('\n')]

    # Part 1
    total_line_sum = 0
    for line in lines:
        parenth_stack = []
        char_list = [x for x in line]
        for i, char in enumerate(char_list):
            if char in ['(', ')']:
                parenth_stack.append((i, char))

        if parenth_stack:
            while parenth_stack:
                for i, parenth in enumerate(parenth_stack):
                    first_parenth = parenth_stack[i]
                    second_parenth = parenth_stack[i+1]
                    if first_parenth[1] == '(' and second_parenth[1] == ')':
                        in_parenth = char_list[first_parenth[0]+1:second_parenth[0]]
                        result = evaluate_char_list(in_parenth)
                        for index in range(first_parenth[0], second_parenth[0]+1):
                            char_list.pop(first_parenth[0])
                        char_list.insert(first_parenth[0], result)
                        parenth_stack.pop(i)
                        parenth_stack.pop(i)
                        break
                if '(' not in char_list and ')' not in char_list:
                    break
                parenth_stack = []
                for i, char in enumerate(char_list):
                    if char in ['(', ')']:
                        parenth_stack.append((i, char))

        line_result = evaluate_char_list(char_list, return_type='int')
        total_line_sum += line_result
    print(f'Answer to part 1: {total_line_sum}')

    # Part 2
    total_line_sum = 0
    for line in lines:
        parenth_stack = []
        char_list = [x for x in line]
        for i, char in enumerate(char_list):
            if char in ['(', ')']:
                parenth_stack.append((i, char))

        if parenth_stack:
            while parenth_stack:
                for i, parenth in enumerate(parenth_stack):
                    first_parenth = parenth_stack[i]
                    second_parenth = parenth_stack[i+1]
                    if first_parenth[1] == '(' and second_parenth[1] == ')':
                        in_parenth = char_list[first_parenth[0]+1:second_parenth[0]]
                        result = evaluate_char_list_v2(in_parenth)
                        for index in range(first_parenth[0], second_parenth[0]+1):
                            char_list.pop(first_parenth[0])
                        char_list.insert(first_parenth[0], result)
                        parenth_stack.pop(i)
                        parenth_stack.pop(i)
                        break
                if '(' not in char_list and ')' not in char_list:
                    break
                parenth_stack = []
                for i, char in enumerate(char_list):
                    if char in ['(', ')']:
                        parenth_stack.append((i, char))

        line_result = evaluate_char_list_v2(char_list, return_type='int')
        total_line_sum += line_result
    print(f'Answer to part 2: {total_line_sum}')
