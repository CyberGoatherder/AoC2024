# Setup the input
with open("input.txt") as file:
    lines = file.readlines()

# Convert lines into lists of integers
numbers_per_line = [list(map(int, line.split())) for line in lines]

# Valid counter
safe_count = 0

# For loop to go line by line
for i, line in enumerate(numbers_per_line, start=1):
    valid_line = True
    direction = "neutral"
    # For loop to compare each number in the line, number by number
    for j in range(len(line) - 1):
        prev_direction = direction
        current_num = line[j]
        next_num = line[j + 1]
        # Check difference is not outside 1 - 3, if it is, break and go to the next line
        if abs(current_num - next_num) > 3 or abs(current_num - next_num) < 1:
            valid_line = False
            break
        # Check current direction
        if current_num > next_num:
            direction = "down"
        else:  
            direction = "up"
        # Check if direction has changed, if it has, break and go to the next line
        if direction != prev_direction and prev_direction != "neutral":
            valid_line = False
            break
    # We only reach this point if all checks pass, thus, we add 1 to the safe counter and move on to the next line
    if valid_line == True:
        safe_count += 1

solution = safe_count
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")