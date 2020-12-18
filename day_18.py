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

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_18.txt') as f:
        file_data = f.read()
        
    # Format the input
    lines = [x.replace(' ', '') for x in file_data.split('\n')]

    # Part 1
    total_line_sum = 0
    for line in lines:
        parenth_stack = []
        char_list = [x for x in line]
        print(char_list)
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
                        print(char_list)
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

    import pdb;pdb.set_trace()
