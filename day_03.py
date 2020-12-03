from functools import reduce

TREE = "#"

def count_trees(map, move_x, move_y):
    position = [0, 0]
    tree_count = 0
    row_length = len(map[0])

    while position[1] < len(map) -1:
        position[0] += move_x
        position[1] += move_y

        if position[0] >= row_length:
            position[0] = position[0] - row_length

        if map[position[1]][position[0]] == TREE:
            tree_count += 1
    return tree_count


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_03.txt') as f:
        file_data = f.read()
    map = [[y for y in x] for x in file_data.split('\n')]

    # Part 1
    move_x = 3
    move_y = 1
    tree_count = count_trees(map, move_x, move_y)
    print(f"Answer to part 1: {tree_count}")

    # Part 2
    move_combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = []
    for move_x, move_y in move_combinations:
        results.append(count_trees(map, move_x, move_y))

    print(f"Answer to part 2: {reduce(lambda x, y: x*y, results)}")
