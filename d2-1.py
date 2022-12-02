rock_pts = 1
paper_pts = 2
scissor_pts = 3

loss_pts = 0
draw_pts = 3
win_pts = 6

opponent_choices = {'A' : 'Rock', 'B' : 'Paper', 'C' : 'Scissors'}
player_choices = {'X' : 'Rock', 'Y' : 'Paper', 'Z' : 'Scissors'}
choice_points = {'Rock' : 1, 'Paper' : 2, 'Scissors' : 3}

with open('inputs/d2-1.txt') as file:
    total_points = 0
    for line in file:
        round = line.split()
        opp_choice = opponent_choices[round[0]]
        player_choice = player_choices[round[1]]
        total_points += choice_points[player_choice]

        # there's a fast way to do this for sure, but might go through the cases for now
        if opp_choice == player_choice:
            total_points += draw_pts
        else:
            if opp_choice == 'Rock' and player_choice == 'Paper':
                total_points += win_pts
            elif opp_choice == 'Paper' and player_choice == 'Scissors':
                total_points += win_pts
            elif opp_choice == 'Scissors' and player_choice == 'Rock':
                total_points += win_pts

print(total_points)