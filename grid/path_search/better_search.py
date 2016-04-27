def create_graph(num_rows, num_columns):
    graph = {}
    for row_number in range(0, num_rows):
        for column_number in range(0, num_columns):
            graph[(row_number, column_number)] = find_neighbours([row_number, column_number], num_rows, num_columns)
    return graph


def find_neighbours(cell, num_rows, num_cols):
    # in a grid can move up, or left
    possible_directions = [[-1, 0], [0, -1]]
    neighbours = []
    for direction in possible_directions:
        neighbour = [cell[0] + direction[0], cell[1] + direction[1]]
        if 0 <= neighbour[0] < num_rows and 0 <= neighbour[1] < num_cols:
            neighbours.append(neighbour)
    return neighbours


def search(input_grid):
    # create graph
    num_rows = len(input_grid)
    num_columns = len(input_grid[0])
    graph = create_graph(num_rows, num_columns)

    # reverse search grid so end point is top left, start bottom right
    goal = [0, 0]
    current_cell = [num_rows-1, num_columns-1]

    # find possible next directions, and 'height' of current cell
    next_directions = graph[(current_cell[0], current_cell[1])]
    current_height = input_grid[current_cell[0]][current_cell[1]]

    # initialise list to store resulting steps
    path = ''

    # loop until reach top left
    while not (current_cell == goal):
        if len(next_directions) > 1:
            # find the heights of the cells next to current cell
            optional_heights = [(input_grid[cell[0]][cell[1]], cell) for cell in next_directions]
            # calculate the difference between them to find least cost step
            height_differences = [(abs(new_height-current_height), cell) for new_height, cell in optional_heights]
            # find the cell with minimum cost
            next_cell = [cell for height, cell in height_differences if height == min(height for height, _ in height_differences)][0]
        else:
            next_cell = next_directions[0]

        # find which direction the next step is in and add it to path
        direction = get_inverse_direction(current_cell, next_cell)
        path+=direction

        # update values for current location and height
        current_cell = next_cell
        current_height = input_grid[current_cell[0]][current_cell[1]]
        next_directions = graph[(current_cell[0], current_cell[1])]

    # return reversed path to show path from top left to bottom right
    return path[::-1]


def get_inverse_direction(current_cell, next_cell):
    direction = [next_cell[0] - current_cell[0], next_cell[1] - current_cell[1]]
    if direction == [-1, 0]:
        return 'd'
    if direction == [0, -1]:
        return 'r'


if __name__ == '__main__':
    grid2 = [
        [0x46B, 0xE59, 0xEA, 0xC1F, 0x45E, 0x63],
        [0x899, 0xFFF, 0x926, 0x7AD, 0xC4E, 0xFFF],
        [0xE2E, 0x323, 0x6D2, 0x976, 0x83F, 0xC96],
        [0x9E9, 0xA8B, 0x9C1, 0x461, 0xF74, 0xD05],
        [0xEDD, 0xE94, 0x5F4, 0xD1D, 0xD03, 0xDE3],
        [0x89, 0x925, 0xCF9, 0xCA0, 0xF18, 0x4D2]]
    grid3 = [[1131, 3673, 234, 3103, 1118, 99],
    [2201, 4095, 2342, 1965, 3150, 4095],
    [3630, 803, 1746, 2422, 2111, 3222],
    [2537, 2699, 2497, 1121, 3956, 3333],
    [3805, 3732, 1524, 3357, 3331, 3555],
    [137, 2341, 3321, 3232, 3864, 1234]]

    grid = [[1, 2, 3],
    [9, 7, 15],
    [4, 10, 9]]
    print search(grid3)
