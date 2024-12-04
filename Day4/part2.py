# Setup the input
def parse_map():
    with open("input.txt") as file:
        # Create a list of lists, one list per line, then we can map any character 
        # for example grid[0][0] will be the first character of the first line
        grid = []
        for line in file.readlines():
            grid.append(list(line))
    return grid

def check_for_xmas(grid, a_row, a_col, xmas_count):
    # Check our cross shape remains inside of our grid
    if (a_row - 1 >= 0 and a_row + 1 < len(grid) and
        a_col - 1 >= 0 and a_col + 1 < len(grid[a_row])):
        # Get the characters in the cross
        ul = grid[a_row - 1][a_col - 1] # up-left
        ur = grid[a_row - 1][a_col + 1] # up-right
        dl = grid[a_row + 1][a_col - 1] # down-left
        dr = grid[a_row + 1][a_col + 1] # down-right
        # Now check it's a valid X-MAS cross
        if (((ul == 'M' and dr == 'S') or (ul == 'S' and dr == 'M')) and
            ((ur == 'M' and dl == 'S') or (ur == 'S' and dl == 'M'))):
                xmas_count += 1
    return xmas_count

def check_for_a(grid):
    xmas_count = 0
    # Nested loop to loop through each character in the grid looking for 'A'
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If we find an 'A' we then pull the cross shape
            if grid[row][col] == 'A':
                xmas_count = check_for_xmas(grid, row, col, xmas_count)
    return xmas_count

def main():
    grid = parse_map()
    solution = check_for_a(grid)
    print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")

if __name__ == "__main__":
    main()