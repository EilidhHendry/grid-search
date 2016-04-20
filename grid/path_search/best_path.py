import sys

def find_cost_grid(cost_grid, num_rows, num_cols):
    # create empty grid to keep cost in (TODO: dynamically create to save mem)
    total_cost = [[0 for x in range(num_cols)] for x in range(num_rows)]

    # find start point
    total_cost[0][0] = cost_grid[0][0]

    # find end coordinate
    m, n = num_rows-1, num_cols-1

    # initialize first column of costs
    for i in range(1, m+1):
        total_cost[i][0] = total_cost[i-1][0] + cost_grid[i][0]

    # initialize first row
    for j in range(1, n+1):
        total_cost[0][j] = total_cost[0][j-1] + cost_grid[0][j]

    # Find rest of total costs
    for i in range(1, m+1):
        for j in range(1, n+1):
            total_cost[i][j] = min(total_cost[i-1][j], total_cost[i][j-1]) + cost_grid[i][j]

    return total_cost

def find_path(cost_grid, num_rows, num_columns):
    # Initialize path
    path = ''
    # initialize start coordinates
    current_row = 0
    current_column = 0
    # end coordinate
    m = num_rows-1
    n = num_columns-1

    # loop until reach end coordinate
    while not (current_row, current_column) == (m, n):

        # try will fail when there is no right/down movement possible
        try:
            right_cost = cost_grid[current_row][current_column+1]
        except:
            right_cost = sys.maxint
        try:
            down_cost = cost_grid[current_row+1][current_column]
        except:
            down_cost = sys.maxint

        # find the minimum cost step
        step = min(right_cost, down_cost)
        if step == right_cost:
            path+='r'
            current_column+=1

        if step == down_cost:
            path+='d'
            current_row+=1

    return path

def grid_search(input_grid):
    num_rows = len(input_grid)
    num_columns = len(input_grid[0])
    cost_grid = find_cost_grid(input_grid, num_rows, num_columns)
    path = find_path(cost_grid, num_rows, num_columns)
    return path
