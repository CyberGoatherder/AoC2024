import re

# Setup the input
with open("input.txt") as file:
    content = file.read()
    # Add "do()" to the start and move everything onto a single line (Because by default operations are "enabled")
    content = "do()" + content.replace('\n', '')
    # Add newline before each do()
    content = content.replace('do()', '\ndo()')
    # Add newline before each don't()
    content = content.replace('don\'t()', '\ndon\'t()')

    # Iterate over each line of 'content', adding only the lines that start with "do()" to a new list
    # Effectively removing all sections that started with "don't()"
    do_lines = []
    for line in content.splitlines():
        if line.startswith("do()"):
            do_lines.append(line)

    # So now we can just re-run the part1 code against our modified input

    # Regular expression to match "mul(num1,num2)"
    # Using two capture groups to return the two numbers only
    pattern = r"mul\((\d+),(\d+)\)"

    solution = 0

    # One line at a time, look for matches
    for line in do_lines:
        matches = re.findall(pattern, line)
        # match by match, convert to int, multiply and add to running total
        for match in matches:
            num1, num2 = map(int, match)
            solution += num1 * num2

    print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")