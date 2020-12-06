from functools import reduce
from collections import Counter

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_06.txt') as f:
        file_data = f.readlines()

    # Part 1
    tracker_list = []
    group_set = set()
    counter = []
    for i, line in enumerate(file_data):
        chars = line.replace('\n', '')
        if chars == '':
            tracker_list.append(group_set)
            counter.append(len(group_set))
            group_set = set()
        else:
            for char in chars:
                group_set.add(char)

        if i + 1 == len(file_data):
            tracker_list.append(group_set)
            counter.append(len(group_set))

    print(f"Answer to part 1: {reduce(lambda x, y: x+y, counter)}")

    # Part 2
    num_in_group = 0
    group_string = ''
    tracker_list = []
    for i, line in enumerate(file_data):
        chars = line.replace('\n', '')

        if chars == '':
            tracker_list.append({'num_in_group': num_in_group, 'group_count': Counter(group_string)})
            group_string = ''
            num_in_group = 0
        else:
            num_in_group += 1
            for char in chars:
                group_string = group_string + char

        if i + 1 == len(file_data):
            tracker_list.append({'num_in_group': num_in_group, 'group_count': Counter(group_string)})

    count_list = []
    for detail_dict in tracker_list:
        num_in_group = detail_dict['num_in_group']
        group_count = detail_dict['group_count']
        number_answer_the_same = [x for x in group_count if group_count[x] == num_in_group]
        count_list.append(len(number_answer_the_same))

    print(f"Answer to part 2: {reduce(lambda x, y: x+y, count_list)}")
