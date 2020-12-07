if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_07.txt') as f:
        file_data = f.read()
    lines = file_data.split('\n')

    # Parse it into a dict
    rules_dict = {}
    for line in lines:
        split_line = line.strip().split(' bags contain ')
        container = split_line[0]
        content = {}
        for contents in split_line[1].split(', '):
            if contents != 'no other bags.':
                words = contents.split(' ')
                content[words[1] + ' ' + words[2]] = int(words[0])
        rules_dict[container] = content

    # Part 1
    start_bag = 'shiny gold'
    bags = set([start_bag])
    num_added_bags = 0

    while len(bags) > num_added_bags:
        num_added_bags = len(bags)
        for bag in rules_dict:
            if any(color in rules_dict[bag].keys() for color in bags):
                bags.add(bag)

    part_1_answer = len(bags) - 1  # Remove the 'shiny gold' bag from the count
    print(f'Answer to part 1: {part_1_answer}')

    # Part 2
    bags = {}
    queue = [(start_bag, 1)]

    while len(queue) > 0:
        color, quantity = queue.pop(-1)
        for colour_key in rules_dict[color]:
            new_quantity = rules_dict[color][colour_key] * quantity
            queue.append((colour_key, new_quantity))
            if bags.get(colour_key, None) is not None:
                bags[colour_key] += new_quantity
            else:
                bags[colour_key] = new_quantity

    print(f'Answer to part 2: {sum(bags.values())}')
