# Setup the input
with open("input.txt") as file:
    lines = file.readlines()

order = []
books = []

for line in lines:
    # Split order lines
    if '|' in line:
        left, right = map(int, line.strip().split('|'))
        order.append((left, right))
    # Split page lines
    elif ',' in line:
        number_strings = line.strip().split(',')
        page_numbers = []
        for num_str in number_strings:
            page_numbers.append(int(num_str))
        books.append(page_numbers)

# Now find the valid books
valid_books = []
# We go one 'book' at a time
for book in books:
    is_valid = True
    # Then we go through each page in each book
    for page in book:
        # Set the current page
        current_page = page
        # Get the valid previous and next pages based on the current page against all of the order rules
        valid_previous_pages = []
        valid_next_pages = []
        for rule in order:
            if rule[1] == current_page:
                valid_previous_pages.append(rule[0])
            if rule[0] == current_page:
                valid_next_pages.append(rule[1])
        # If there is a "next page", check if it is valid by comparing it to the valid next pages, if not, set to false and break
        if book.index(current_page) + 1 < len(book):
            next_page = book[book.index(current_page) + 1]
            if next_page not in valid_next_pages:
                is_valid = False
                break
        # If there is a "previous page", check if it is valid by comparing it to the valid previous pages, if not, set to false and break
        if book.index(current_page) > 0:
            prev_page = book[book.index(current_page) - 1]
            if prev_page not in valid_previous_pages:
                is_valid = False
                break
    # If the flag has remained "True" we know the book is valid, append it to the valid books list
    if is_valid:
        valid_books.append(book)

# Now we sum the middle page of each valid book
middle_page_sum = 0
for book in valid_books:
    middle_page = book[len(book) // 2]
    middle_page_sum += middle_page

# Print the solution
solution = middle_page_sum
print(f"\n\033[92m[+] Solution: {solution}\033[0m\n")