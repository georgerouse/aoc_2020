from collections import Counter
from copy import deepcopy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'

def print_floor_map(floor_map):
    for row in floor_map:
        print(''.join(row))

test = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

def get_adjacent_seats_v1(x, y, floor_map):
    y_max_index = len(floor_map) - 1
    x_max_index = len(floor_map[0]) - 1
    seat_list = []

    if x - 1 >= 0:
        seat_list.append(floor_map[y][x - 1])
    if x + 1 <= x_max_index:
        seat_list.append(floor_map[y][x + 1])
    if y - 1 >= 0:
        seat_list.append(floor_map[y - 1][x])
    if y + 1 <= y_max_index:
        seat_list.append(floor_map[y + 1][x])

    if x - 1 >= 0 and y - 1 >= 0:
        seat_list.append(floor_map[y - 1][x - 1])
    if x - 1 >= 0 and y + 1 <= y_max_index:
        seat_list.append(floor_map[y + 1][x - 1])

    if x + 1 <= x_max_index and y - 1 >= 0:
        seat_list.append(floor_map[y - 1][x + 1])
    if x + 1 <= x_max_index and y + 1 <= y_max_index:
        seat_list.append(floor_map[y + 1][x + 1])

    return seat_list


def get_adjacent_seats_v2(x, y, floor_map, debug=False):
    y_max_index = len(floor_map) - 1
    x_max_index = len(floor_map[0]) - 1
    seat_list = []
    offsets = (
        (0, -1), (0, 1), (-1, 0), (1, 0),
        (1, -1), (1, 1), (-1, -1), (-1, 1)
    )
    for x_offset, y_offset in offsets:
        seat_not_found = True
        x_search = x + x_offset
        y_search = y + y_offset
        seat_found = None
        while seat_not_found and \
              x_search <= x_max_index and \
              x_search >= 0 and \
              y_search <= y_max_index and \
              y_search >= 0:
            if floor_map[y_search][x_search] == FLOOR:
                x_search = x_search + x_offset
                y_search = y_search + y_offset
            else:
                seat_not_found = False
                seat_found = floor_map[y_search][x_search]

        if seat_found is not None:
            seat_list.append(seat_found)
        if debug:
            print(f'Offset: {x_offset, y_offset}, seat found {seat_found}')

    return seat_list

def count_occupied_seats(floor_map):
    occupied_count = 0
    for y, row in enumerate(floor_map):
        for x, seat in enumerate(row):
            if floor_map[y][x] == OCCUPIED_SEAT:
                occupied_count += 1
    return occupied_count

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_11.txt') as f:
        file_data = f.read()
    floor_map = file_data.split('\n')
    floor_map = [[y for y in x] for x in floor_map]
    floor_map_copy = deepcopy(floor_map)

    # Part 1
    map_not_equal = True
    while map_not_equal:
        updated_map = deepcopy(floor_map)
        for y, row in enumerate(floor_map):
            for x, seat in enumerate(row):
                adjacent_seats = get_adjacent_seats_v1(x, y, floor_map)

                if seat == EMPTY_SEAT and OCCUPIED_SEAT not in adjacent_seats:
                    updated_map[y][x] = OCCUPIED_SEAT

                elif seat == OCCUPIED_SEAT:
                    adjacent_seat_count = Counter(adjacent_seats)
                    occupied_seat_count = adjacent_seat_count.get(OCCUPIED_SEAT)
                    if occupied_seat_count and occupied_seat_count >= 4:
                         updated_map[y][x] = EMPTY_SEAT

        if floor_map == updated_map:
            map_not_equal = False
        else:
            floor_map = updated_map

    print(f'Answer to part 1: {count_occupied_seats(floor_map)}')

    # Part 2
    floor_map = floor_map_copy
    map_not_equal = True
    while map_not_equal:
        updated_map = deepcopy(floor_map)
        for y, row in enumerate(floor_map):
            for x, seat in enumerate(row):
                adjacent_seats = get_adjacent_seats_v2(x, y, floor_map)
                if seat == EMPTY_SEAT and OCCUPIED_SEAT not in adjacent_seats:
                    updated_map[y][x] = OCCUPIED_SEAT

                elif seat == OCCUPIED_SEAT:
                    adjacent_seat_count = Counter(adjacent_seats)
                    occupied_seat_count = adjacent_seat_count.get(OCCUPIED_SEAT)
                    if occupied_seat_count and occupied_seat_count >= 5:
                         updated_map[y][x] = EMPTY_SEAT

        if floor_map == updated_map:
            map_not_equal = False
        else:
            floor_map = updated_map

    print(f'Answer to part 2: {count_occupied_seats(floor_map)}')
