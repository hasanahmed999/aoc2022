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
for i in range(1, 99-1):
    for j in range(1, 99-1): # -1 bcs we dont need to check edge
        visible = False
        while visible == False:
            # Up
            for k in range(0, i):
                if grid[k][j] >= grid[i][j]:
                    break
                if k == i-1:
                    visible = True
                    break

            # Down
            for k in range(i+1, 99):
                if grid[k][j] >= grid[i][j]:
                    break
                if k == 98:
                    visible = True
                    break

            # Left
            for k in range(0, j):
                if grid[i][k] >= grid[i][j]:
                    break
                if k == j-1:
                    visible = True
                    break # have to break out of all the for loops .............

            # Right
            for k in range(j+1, 99):
                if grid[i][k] >= grid[i][j]:
                    break
                if k == 98:
                    visible = True
            if visible:
                visible_trees += 1
            else:
                break
                
print(visible_trees)
            
            
        
        