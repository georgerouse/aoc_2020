def find_seat_location(ticket_number):
    number_of_rows = 128
    number_of_columns = 8

    row_string = ticket_number[0:7]
    col_string = ticket_number[7:10]

    row_range = [0, 127]
    for letter in row_string:
        number_of_rows = number_of_rows / 2
        if letter == 'F':
            row_range[1] = row_range[1] - number_of_rows
        else:
            row_range[0] = row_range[0] + number_of_rows

    assert row_range[0] == row_range[1]

    col_range = [0, 7]
    for letter in col_string:
        number_of_columns = number_of_columns / 2
        if letter == 'L':
            col_range[1] = col_range[1] - number_of_columns
        else:
            col_range[0] = col_range[0] + number_of_columns

    assert col_range[0] == col_range[1]

    return row_range[0], col_range[0]


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_05.txt') as f:
        file_data = f.read()
    ticket_list = [x for x in file_data.split('\n')]

    # Part 1
    seat_id_list = []
    highest_seat_id = None
    for ticket in ticket_list:
        row_num, col_num = find_seat_location(ticket)
        seat_id = row_num * 8 + col_num
        seat_id_list.append(int(seat_id))
        if highest_seat_id is None or seat_id > highest_seat_id:
            highest_seat_id = seat_id
    print(f"Answer to part 1: {int(highest_seat_id)}")

    # Part 2
    seat_id_list.sort()
    for i, seat_id in enumerate(seat_id_list):
        if seat_id_list[i+1] != seat_id + 1:
            print(f"Answer to part 2: {seat_id + 1}")
            break
