import re

# Setup the input lists
with open("input.txt") as file:
    lines = file.readlines()

# Regular expression to match "mul(num1,num2)"
# Using two capture groups to return the two numbers only
pattern = r"mul\((\d+),(\d+)\)"

solution = 0

# One line at a time, look for matches
for line in lines:
    matches = re.findall(pattern, line)
    # match by match, convert to int, multiply and add to running total
    for match in matches:
        num1, num2 = map(int, match)
        solution += num1 * num2

print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")