from functools import reduce

def validate_ticket(ticket, field_dict):
    invalid_list = []
    for value in ticket:
        is_valid = False
        for key, dict_values in field_dict.items():
                if (
                    (value >= dict_values[0][0] and value <= dict_values[0][1]) or
                    (value >= dict_values[1][0] and value <= dict_values[1][1])
                ):
                    is_valid = True
        if not is_valid:
            invalid_list.append(value)

    return invalid_list


def is_valid(number, dict_values):
    is_valid = False
    if (
        (number >= dict_values[0][0] and number <= dict_values[0][1]) or
        (number >= dict_values[1][0] and number <= dict_values[1][1])
    ):
        is_valid = True
    return is_valid


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_16.txt') as f:
        file_data = f.read()

    # Format the input
    lines = [x for x in file_data.split('\n')]
    is_nearby_tickets = False
    nearby_tickets = []
    field_dict = {}
    for i, line in enumerate(lines):
        if is_nearby_tickets:
            nearby_tickets.append(line)
        else:
            if line == 'your ticket:':
                my_ticket = lines[i+1]
            elif line == 'nearby tickets:':
                is_nearby_tickets = True
            elif ':' in line:
                field = line.split(': ')[0].replace(' ', '_')
                values = [[int(y) for y in x.split('-')] for x in (line.split(': ')[1].split(' or '))]
                field_dict[field] = values
    nearby_tickets = [[int(y) for y in x.split(',')] for x in nearby_tickets]
    my_ticket = [int(x) for x in my_ticket.split(',')]

    # Part 1
    not_valid_values = []
    for nearby_ticket in nearby_tickets:
        invalid_fields = validate_ticket(nearby_ticket, field_dict)
        if invalid_fields:
            not_valid_values += invalid_fields
    scanning_error_rate = sum(not_valid_values)
    print(f'Answer to part 1: {scanning_error_rate}')

    # Part 2
    # Remove the invalid tickets
    filtered_tickets = []
    for nearby_ticket in nearby_tickets:
        ticket_valid = True
        for number in nearby_ticket:
            if number in not_valid_values:
                ticket_valid = False
        if ticket_valid:
            filtered_tickets.append(nearby_ticket)

    # Deduce the possible indexes for the fields
    possible_indexes = {}
    ticket_length = len(nearby_tickets[0])
    for key, dict_values in field_dict.items():
        possible_index = []
        for i in range(0, ticket_length):
            index_list = [x[i] for x in filtered_tickets]
            valid_list = [is_valid(x, dict_values) for x in index_list]
            if all(valid_list):
                possible_index.append(i)
        possible_indexes[key] = possible_index

    # Filter the possible indexes for the fields to those where it's just one
    complete = False
    final_indexes = {}
    while not complete:
        for key, index_list in possible_indexes.items():
            if len(index_list) == 1:
                index_value = index_list[0]
                final_indexes[key] = index_value
                for other_key, other_index_list in possible_indexes.items():
                    if key != other_key:
                        possible_indexes[other_key] = [x for x in other_index_list if x != index_value]

        if len(final_indexes) == 20:
            complete = True
            break

    dest_indexes = []
    for key, value in final_indexes.items():
        if key.startswith('departure'):
            dest_indexes.append(value)
    dest_values = [x for i, x in enumerate(my_ticket) if i in dest_indexes]
    print(f'Answer to part 2: {reduce(lambda x, y: x*y, dest_values)}')
    import pdb;pdb.set_trace()
