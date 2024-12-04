# Setup the input
def parse_map():
    with open("input.txt") as file:
        # Create a list of lists, one list per line, then we can map any character 
        # for example grid[0][0] will be the first character of the first line
        grid = []
        for line in file.readlines():
            grid.append(list(line))
    return grid

def check_the_rest(grid, m_row, m_col, direction_index, xmas_count):
    directions = [
        (-1, 0),  # up [0]
        (1, 0),   # down [1]
        (0, -1),  # left [2]
        (0, 1),   # right [3]
        (-1, -1), # up-left [4]
        (-1, 1),  # up-right [5]
        (1, -1),  # down-left [6]
        (1, 1)    # down-right [7]
    ]
    y, x = directions[direction_index]
    # Check we remain inside our grid and then for 'A' in same direction
    a_row = m_row + y
    a_col = m_col + x
    if (0 <= a_row < len(grid) and 
        0 <= a_col < len(grid[a_row]) and 
        grid[a_row][a_col] == 'A'):
        # Check we remain inside our grid and then for 'S' in same direction
        s_row = a_row + y
        s_col = a_col + x
        if (0 <= s_row < len(grid) and 
            0 <= s_col < len(grid[s_row]) and 
            grid[s_row][s_col] == 'S'):
            # If we find 'S' we increment our xmas_count by 1 as we have a full match
            xmas_count += 1
    return xmas_count

def check_for_m(grid, row, col, xmas_count):
    directions = [
        (-1, 0),  # up (0)
        (1, 0),   # down [1]
        (0, -1),  # left [2]
        (0, 1),   # right [3]
        (-1, -1), # up-left [4]
        (-1, 1),  # up-right [5]
        (1, -1),  # down-left [6]
        (1, 1)    # down-right [7]
    ]
    # Loop through each direction returning the index of the list and split the coords into y, x
    for direction_index, (y, x) in enumerate(directions):
        m_row = row + y
        m_col = col + x
        # Check the new position is firstly, inside of the grid and matches the character "M"
        if (0 <= m_row < len(grid) and 
            0 <= m_col < len(grid[m_row]) and 
            grid[m_row][m_col] == "M"):
            # If found, we now check for the rest of the letters in the same direction specified by the 'direction_index'
            xmas_count = check_the_rest(grid, m_row, m_col, direction_index, xmas_count)
    return xmas_count

def check_for_x(grid):
    xmas_count = 0
    # Nested loop to loop through each character in the grid looking for 'X'
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If we find an 'X' we then check for "M"
            if grid[row][col] == 'X':
                xmas_count = check_for_m(grid, row, col, xmas_count)
    return xmas_count

def main():
    grid = parse_map()
    solution = check_for_x(grid)
    print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")

if __name__ == "__main__":
    main()