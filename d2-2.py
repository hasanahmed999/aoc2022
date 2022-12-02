rock_pts = 1
paper_pts = 2
scissor_pts = 3

loss_pts = 0
draw_pts = 3
win_pts = 6

opponent_choices = {'A' : 'Rock', 'B' : 'Paper', 'C' : 'Scissors'}
player_choices = {'X' : 'Loss', 'Y' : 'Draw', 'Z' : 'Win'}
choice_points = {'Rock' : 1, 'Paper' : 2, 'Scissors' : 3}
RPS = ['Rock', 'Paper', 'Scissors']

with open('inputs/d2-1.txt') as file:
    total_points = 0
    for line in file:
        round = line.split()
        opp_choice = opponent_choices[round[0]]    
        outcome = player_choices[round[1]]
        
        if outcome == 'Loss':
            player_choice = RPS[ RPS.index(opp_choice) - 1 ]
            total_points += choice_points[player_choice]
        elif outcome == 'Draw':
            player_choice = opp_choice
            total_points += choice_points[player_choice]
            total_points += draw_pts
        else:
            # edge case
            if opp_choice == 'Scissors':
                player_choice = 'Rock'
            else:
                player_choice = RPS[ RPS.index(opp_choice) + 1 ]
            total_points += choice_points[player_choice]
            total_points += win_pts


print(total_points)