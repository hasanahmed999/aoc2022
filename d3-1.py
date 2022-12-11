import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)


with open('inputs/d3-1.txt') as file:
    total_priority = 0
    for line in file:
        first_half = line[:len(line)//2:]
        second_half = line[len(line)//2::]

        # https://bobbyhadz.com/blog/python-find-common-characters-between-two-strings
        common_letter = ''.join(
            set(first_half).intersection(second_half)
        )

        total_priority += letters.index(common_letter) + 1

print(total_priority) 