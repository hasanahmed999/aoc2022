import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)


with open('inputs/d3-1.txt') as file:
    total_priority = 0
    first_group = []
    second_group = []

    for line in file:
        if len(first_group) < 3:
            first_group.append(line.strip())
        else:
            second_group.append(line.strip())


        if len(first_group) == 3 and len(second_group) == 3:            
            # First group
            common_letter_g1 = ''.join(
                set(first_group[0]).intersection(first_group[1]).intersection(first_group[2])
            )

            # Second group
            common_letter_g2 = ''.join(
                set(second_group[0]).intersection(second_group[1]).intersection(second_group[2])
            )

            # Reset groups at end of algorithm
            total_priority += letters.index(common_letter_g1) + 1 + letters.index(common_letter_g2) + 1
            first_group.clear()
            second_group.clear()

print(total_priority) 