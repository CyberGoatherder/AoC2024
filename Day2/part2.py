# Setup the input
with open("input.txt") as file:
    lines = file.readlines()

# Convert lines into lists of integers
numbers_per_line = [list(map(int, line.split())) for line in lines]

# Valid counter
safe_count = 0

# Function to check if a line is safe
def is_line_safe(line):
    direction = "neutral"
    for j in range(len(line) - 1):
        prev_direction = direction
        current_num = line[j]
        next_num = line[j + 1]
        # Check difference is not outside 1 - 3
        if abs(current_num - next_num) > 3 or abs(current_num - next_num) < 1:
            return False
        # Check current direction
        if current_num > next_num:
            direction = "down"
        else:
            direction = "up"
        # Check if direction has changed
        if direction != prev_direction and prev_direction != "neutral":
            return False
    return True

# For loop to go line by line
for i, line in enumerate(numbers_per_line, start=1):
    if is_line_safe(line):
        safe_count += 1
    else:
        # Remove one number of the failed line at a time to see if it can become valid
        line_is_safe = False
        for k in range(len(line)):
            # Take the line from the beginning up to (but not including) K 
            # and then join it with positions k + 1 onwards, thus removing K from the list
            modified_line = line[:k] + line[k + 1:]
            if is_line_safe(modified_line):
                line_is_safe = True
                break
        if line_is_safe:
            safe_count += 1

print(safe_count)