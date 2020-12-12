class Ferry:
    def __init__(self, facing=90):
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        self.facing = facing

    def print_details(self):
        print(f'North: {self.north}\nSouth: {self.south}')
        print(f'West: {self.west}\nEast: {self.east}')
        print(f'Facing: {self.facing}')
        print('=============')

    def move_forward(self, amount):
        if self.facing == 0 or self.facing == 360:
            self.north += amount
        elif self.facing == 90:
            self.east += amount
        elif self.facing == 180:
            self.south += amount
        elif self.facing == 270:
            self.west += amount
        else:
            raise RuntimeError(f'Unknown direction: {self.facing}')

    def turn_left(self, degrees):
        self.facing -= degrees
        if self.facing < 0:
            self.facing += 360

    def turn_right(self, degrees):
        self.facing += degrees
        if self.facing >= 360:
            self.facing -= 360

    def move_north(self, amount):
        self.north += amount

    def move_south(self, amount):
        self.south += amount

    def move_east(self, amount):
        self.east += amount

    def move_west(self, amount):
        self.west += amount

    def man_distance(self):
        if self.north > self.south:
            x = self.north - self.south
        else:
            x = self.south - self.north
        if self.west > self.east:
            y = self.west - self.east
        else:
            y = self.east - self.west
        return x + y


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_12.txt') as f:
        file_data = f.read()
    file_list = file_data.split('\n')
    move_list = []
    for move in file_list:
        move_tuple = (move[0], int(move[1:]))
        move_list.append(move_tuple)

    # Part 1
    ferry = Ferry()
    for action, amount in move_list:
        if action == 'F':
            ferry.move_forward(amount)
        elif action == 'N':
            ferry.move_north(amount)
        elif action == 'S':
            ferry.move_south(amount)
        elif action == 'E':
            ferry.move_east(amount)
        elif action == 'W':
            ferry.move_west(amount)
        elif action == 'L':
            ferry.turn_left(amount)
        elif action == 'R':
            ferry.turn_right(amount)
        else:
            raise RuntimeError(f'Unknown action: {action}')

    print(f'Answer to part 1: {ferry.man_distance()}')

    # Part 2
    # TODO
    
