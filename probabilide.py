import itertools
from copy import deepcopy

teams = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5', 'Team 6', 'Team 7', 'Team 8']
positions = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
position_values = [12, 9, 6, 3, 0, 0, 0, 0]
team_scores = [10, 10, 4, 4, 6, 6, 16, 16] 

def calculate_permutations(scores, depth):
    print(depth)
    if depth > 3:
        return scores
    permutations = list(itertools.permutations(teams, len(teams)))
    res_scores = []
    for permutation in permutations:
        permutation_scores = apply_permutation(scores, permutation)
        res_scores.append(calculate_permutations(permutation_scores, depth + 1))
    return res_scores

def apply_permutation(scores, permutation):
    res = deepcopy(scores)
    for i, team in enumerate(permutation):
        position_value = position_values[i]
        if team == 'Team 1':
            res[0] += position_value
        elif team == 'Team 2':
            res[1] += position_value
        elif team == 'Team 3':
            res[2] += position_value
        elif team == 'Team 4':
            res[3] += position_value
        elif team == 'Team 5':
            res[4] += position_value
        elif team == 'Team 6':
            res[5] += position_value
        elif team == 'Team 7':
            res[6] += position_value
        elif team == 'Team 8':
            res[7] += position_value
    return res
print(calculate_permutations(team_scores, 0))





   
#        print(f"{positions[i]}: {team} - Score: {position_value}")
#    total_score_m1 = team1_score + team2_score
#    total_score_m2 = team3_score + team4_score
#    total_score_m3 = team5_score + team6_score
#    total_score_m4 = team7_score + team8_score
#    print(f"Team 1 Score: {team1_score}")
#    print(f"Team 2 Score: {team2_score}")
#    print(f"Total Score_m1: {total_score_m1}")
#    print(f"Team 3 Score: {team3_score}")
#    print(f"Team 4 Score: {team4_score}")
#    print(f"Total Score_m2: {total_score_m2}")
#    print(f"Team 5 Score: {team5_score}")
#    print(f"Team 6 Score: {team6_score}")
#    print(f"Total Score_m3: {total_score_m3}")
#    print(f"Team 7 Score: {team7_score}")
#    print(f"Team 8 Score: {team8_score}")
#    print(f"Total Score_m4: {total_score_m4}")
#    print('-' * 10)
