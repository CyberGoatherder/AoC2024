# Setup the input lists
with open("input.txt") as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    number1, number2 = line.split('   ')
    list1.append(number1)
    list2.append(number2)

# Now find the similarity between the two lists
match_counters = []

for row in list1:
    counter = 0
    for row2 in list2:
        if int(row) == int(row2):
            counter += 1
    match_counters.append(counter)

# Now math the sum of the similarities
sums = []

for a, b in zip(list1, match_counters):
    sums.append(int(a) * int(b))

print(sum(sums))