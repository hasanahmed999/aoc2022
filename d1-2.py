with open('inputs/d1-1.txt') as file:
    list_of_elves = []
    elf = 0
    calories = 0
    for line in file:
        if line.strip().isdigit():
            calories += int(line)
        else:
            list_of_elves.append(calories)
            elf += 1
            calories = 0


list_of_elves_sorted = sorted(list_of_elves, reverse=True)
print(sum(list_of_elves_sorted[0:3]))