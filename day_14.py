test = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


def apply_value_mask(bin_value, mask_value):
    padded_bin_value = bin_value.replace('0b','').zfill(len(mask_value))
    padded_bin_value = [x for x in padded_bin_value]
    for i, x in enumerate(mask_value):
        if x == '1':
            padded_bin_value[i] = x
        elif x == '0':
            padded_bin_value[i] = x
    bin_value = ''.join(padded_bin_value)

    int_value = int(bin_value, 2)
    return int_value


def get_all_bin_locations(loc_value):
	all_bin_locations = [loc_value]
	for i, value in enumerate(loc_value):
		if value != 'X':
			for bin_location in all_bin_locations:
				bin_location[i] = value
			continue
		new_bin_locations = []
		for bin_number in ('1', '0'):
			for bin_location in all_bin_locations:
				bin_location[i] = bin_number
				new_bin_locations.append(bin_location[:])
		all_bin_locations = new_bin_locations
	return [int(''.join(bin_locations), 2) for bin_locations in all_bin_locations]


def apply_location_mask(loc_value, mask_value):
    loc_value = bin(loc_value)
    padded_loc_value = loc_value.replace('0b','').zfill(len(mask_value))
    padded_loc_value = [x for x in padded_loc_value]
    for i, x in enumerate(mask_value):
        if x == '1':
            padded_loc_value[i] = '1'
        elif x == 'X':
            padded_loc_value[i] = 'X'
    loc_value = ''.join(padded_loc_value)
    return get_all_bin_locations(padded_loc_value)


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_14.txt') as f:
        file_data = f.read()
    #file_data = test
    lines = [x for x in file_data.split('\n')]
    instructions = []
    for line in lines:
        split_line = line.split(' = ')
        if split_line[0] == 'mask':
            split_line.insert(1, None)
            instructions.append(split_line)
        else:
            mem_line = split_line[0].replace(']','').split('[')
            mem_line[1] = int(mem_line[1])
            mem_line.insert(2, int(split_line[1]))
            instructions.append(mem_line)

    # Part 1
    results = {}
    for instruction in instructions:
        if instruction[0] == 'mask':
            mask_value = instruction[2]
        else:
            mem_loc = instruction[1]
            value = instruction[2]
            bin_value = bin(value)
            final_value = apply_value_mask(bin_value, mask_value)
            results[mem_loc] = final_value
    sum_values = sum([x for x in results.values()])
    print(f'Answer to part 1: {sum_values}')

    # Part 2
    results = {}
    for instruction in instructions:
        if instruction[0] == 'mask':
            mask_value = instruction[2]
        else:
            mem_loc = instruction[1]
            value = instruction[2]
            loc_values = apply_location_mask(mem_loc, mask_value)
            for loc_value in loc_values:
                results[loc_value] = value

    sum_values = sum([x for x in results.values()])
    print(f'Answer to part 2: {sum_values}')
