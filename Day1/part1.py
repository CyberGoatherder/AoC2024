# Setup the input lists
with open("input.txt") as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    number1, number2 = line.split('   ')
    list1.append(number1)
    list2.append(number2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Now find the difference between the two lists
difference_list = []

for a, b in zip(sorted_list1, sorted_list2):
    difference = abs(int(a) - int(b))
    difference_list.append(difference)

solution = sum(difference_list)
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")