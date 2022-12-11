with open('inputs/d4-1.txt') as file:
    # now we can just deal with set intersections
    overlap_count = 0
    for line in file:
        elves = line.split(',')
        elf1 = elves[0]
        elf2 = elves[1]
        elf1_lower_bound = int(elf1.split('-')[0])
        elf1_upper_bound = int(elf1.split('-')[1])
        elf2_lower_bound = int(elf2.split('-')[0])
        elf2_upper_bound = int(elf2.split('-')[1])

        elf1_set = set(range(elf1_lower_bound, elf1_upper_bound + 1))
        elf2_set = set(range(elf2_lower_bound, elf2_upper_bound + 1))

        overlap_count += 1 if len(elf1_set.intersection(elf2_set)) != 0 else 0

print(overlap_count)