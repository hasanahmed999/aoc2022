with open('inputs/d8-1.txt') as file:
    # 2d array?
    grid = []
    for line in file:
        # len is 99 bcs i'm lazy and manually checked :)
        grid.append([int(digit) for digit in line if digit != '\n'])


visible_trees = 0
# All trees on edge are visible
# 99 + 99 + 97 + 97, or 98*4
visible_trees += (99-1) * 4


# Interior; just has to be visible from the edge (i.e. any direction), so check up, then down, then left, then right
# this is so ungodly inefficient

best_scenic_score = 0
for i in range(1, 99-1):
    for j in range(1, 99-1): # -1 bcs we dont need to check edge
        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0

        # Up
        for k in range(i-1, 0-1, -1):
            up_count += 1
            if grid[k][j] >= grid[i][j]:
                break           

        # Down
        for k in range(i+1, 99):
            down_count += 1
            if grid[k][j] >= grid[i][j]:
                break

        # Left
        for k in range(j-1, 0-1, -1):
            left_count += 1
            if grid[i][k] >= grid[i][j]:
                break

        # Right
        for k in range(j+1, 99):
            right_count += 1
            if grid[i][k] >= grid[i][j]:
                break

        scenic_score = up_count*down_count*left_count*right_count

        best_scenic_score = max(scenic_score, best_scenic_score)

                
print(best_scenic_score)
            
            
        
        