with open('inputs/d1-1.txt') as file:
	calories = 0
	max_calories = 0
	elf = 0
	for line in file:
		if line.strip().isdigit():
			calories += int(line)
		else:
			max_calories = max(max_calories, calories)
			calories = 0


print(max_calories)