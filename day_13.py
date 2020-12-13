import math

test = '''939
7,13,x,x,59,x,31,19'''

def calculate_next_departure(earliest_timestamp, number):
    next_time = earliest_timestamp / number
    multiplier = math.ceil(next_time)
    return number * multiplier

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_13.txt') as f:
        file_data = f.read()
    #file_data = test
    lines = [x for x in file_data.split('\n')]

    # Part 1
    earliest_timestamp = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != 'x']
    depart_times = [calculate_next_departure(earliest_timestamp, x) for x in buses]
    earliest_index = depart_times.index(min(depart_times))
    print(f'Answer to part 1: {buses[earliest_index] * (depart_times[earliest_index] - earliest_timestamp)}')

    # Part 2
    buses = lines[1].split(',')
    buses = [int(x) if x != 'x' else x for x in buses]

    start_time = 0
    multiplier = 1

    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        while((start_time + i) % bus != 0):
            start_time += multiplier
        multiplier *= bus
        
    print(f'Answer to part 2: {start_time}')
