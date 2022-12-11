with open('inputs/d4-1.txt') as file:
    # Take the lowest and highest num if they're from the same set
    # if set1 lower bound is < set 2 lower bound and set 1 upper bound > set 2 upper bound
    # there's full overlap

    # vice versa if set 2's bigger than set 1
    overlap_count = 0
    for line in file:
        elves = line.split(',')
        elf1 = elves[0]
        elf2 = elves[1]

        elf1_lower_bound = int(elf1.split('-')[0])
        elf1_upper_bound = int(elf1.split('-')[1])
        elf2_lower_bound = int(elf2.split('-')[0])
        elf2_upper_bound = int(elf2.split('-')[1])

        # Checks:
        if (elf1_lower_bound <= elf2_lower_bound and elf1_upper_bound >= elf2_upper_bound) or \
           (elf2_lower_bound <= elf1_lower_bound and elf2_upper_bound >= elf1_upper_bound):
           overlap_count += 1

print(overlap_count)